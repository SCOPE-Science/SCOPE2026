import numpy as np
rng = np.random.default_rng(20261020)
angles = [0., .15, .4, 1., 1.5, 2., 2.5, np.pi]
count = 0
for theta in angles:
    m = np.array([[1., 1.], [1., np.exp(1j * theta)]])
    k = 1 / np.cos(theta / 4)
    x = np.array([[1., 1.], [1., -np.exp(-1j * theta)]])
    y = x * m
    sx = np.linalg.svd(x, compute_uv=False)
    sy = np.linalg.svd(y, compute_uv=False)
    ratio = max(sy[0], 2 * sy[1]) / sx.sum()
    assert abs(ratio - k) < 3.e-12
    for _ in range(10):
        z = rng.normal(size=(5000, 2, 2)) + 1j * rng.normal(size=(5000, 2, 2))
        s0 = np.linalg.svd(z, compute_uv=False)
        s1 = np.linalg.svd(z * m, compute_uv=False)
        observed = np.maximum(s1[:, 0], 2 * s1[:, 1]) / s0.sum(axis=1)
        assert np.all(observed < k + 1.e-10)
        count += len(z)
print('PASS:', count, 'deterministic complex samples; all sharp witnesses')
