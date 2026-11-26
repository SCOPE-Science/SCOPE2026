# Independent mathematical audit

## correctness

PASS

The fixed-size ODE is exactly the normalization of (3.3) and (3.4) stated in the record, with g'(0)=1, R0=1, and Jacobian rows (−1/2,1/2), (1,−1). The matching plus two s-sets realizes the claimed regular hypergraph. The square is forward invariant, and strict positivity at finite times follows, e.g., from x'≥−x and y'≥−y inside it. For V=x+y/2, 2V'=f−x−x²−(x+f)y; f≤x, and only the origin can stay on x=0, so LaSalle gives extinction. The arctangent remainder implies −KV²≤V'≤0. For z'=−a(t)z+O(V^j), a(t)≥a0>0 eventually, setting w=z/V^j gives w'=(−a−j V'/V)w+O(1), whose linear coefficient is eventually at most −a0/2 since V→0. Thus z=O(V^j), independently validating the slow-variation estimate. Subtracting the ODEs gives d'=−(3+x)d/2+(f−x)(1−x−d) for d=y−x. Apply the estimate with j=3, giving d=O(V³) and x∼2V/3. With A=−2s²/9 the cubic term of (d−Ax³)' cancels and the remaining forcing is O(x⁴); the same estimate gives d=Ax³+O(x⁴). Therefore u=1/x has u'=1+s²/(9u)+O(u⁻²), first u∼t, then u=t+O(log t). Subtracting the printed logarithm leaves an integrable derivative O(log t/t²), proving a finite intercept for every strict interior start and the difference-of-sizes limit. The submitted symbolic/finite-time checks were inspected, not executed, and are not used as asymptotic proof.

## originality

PASS

The distinct content is the explicit, trajectory-wide second-order asymptotic of the printed critical system, not the model, its threshold, or the use of a cubic slow-mode reduction. The closest same-model result stops at a leading critical profile; the closest two-term laws concern different dynamical systems.

## value

PASS

Addresses the omitted equality regime of a published deterministic closure. The first term resolving these fixed sizes is strictly beyond both linearization and leading decay, so the exact coefficient explains an actual limitation of those summaries. This is an asymptotic distinction within the specified model, not an inference guarantee for noisy observations or a stochastic epidemic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
