# Independent audit — 2026-09-28

Record: `2026/09/11/037`  
Audited tree: `ae3e777e55a91d435e3395bab90f4686967ccf8b`  
Disposition: **repaired**

## Correctness

A fresh reconstruction reproduces the 192x400 CSS matrices, ranks 186/186, zero orthogonality violations, numerical `s2=2.72800676...`, exact inertia `(47,1,0)` at `2.73^2` and `(39,9,0)` at `2.70^2`, classical distance 8, and the explicit weight-7 logical.

The original transfer argument has one substantive monotonicity error: `s2<=2.73` makes `9/s2^2 >= 9/2.73^2`; it cannot justify “at most 1.2076.” Fortunately the exact `2.70` inertia certificate supplies the opposite bound actually needed: `s2>2.70`, hence `9/s2^2 < 100/81≈1.23457<1.5`. The guarded repair rewrites the transfer artifact and all affected prose and removes theorem-like window-wide wording.

## Originality and value

Searches of finite-length lifted-product and moderate-length quantum Tanner literature did not locate this exact shift matrix or certificates. The defensible contribution is an instance-level negative design certificate, not an optimality result for all lift-16 matrices.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/037 ; https://arxiv.org/abs/2503.07567 ; https://arxiv.org/abs/2502.20297 ; https://doi.org/10.1109/18.556667
