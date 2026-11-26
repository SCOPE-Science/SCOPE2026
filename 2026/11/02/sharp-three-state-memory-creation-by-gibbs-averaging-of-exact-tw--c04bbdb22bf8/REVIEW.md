# Independent mathematical audit

## correctness

PASS

Independently reconstructed the extremal reduction in RESULT.md. In the orthonormal centered basis (1,−1,0)/√2 and (−1,−1,2)/√6, doubly stochasticity separates the constant eigenvector, P²=Π forces centered trace zero, and the trace-one stochastic parameterization has centered entries −τ,τ on the diagonal and √3(t−r∓d)/2 off the diagonal, with τ=(3s−1)/2, s=P33, r=1−s. Centered determinant zero, equivalently square zero with trace zero, gives d²=(t−r)²+3(s−1/3)². Nonnegativity is exactly |d|≤2s and |d|≤r−|t−r|, giving √3|s−1/3|≤min(2s,1−s), with equality-compatible witnesses at t=r and d=√3(s−1/3). Solving both inequalities gives (2√3−3)/3≤s≤1/√3. The witnesses are strictly positive in the interior and square to Π including at both endpoints. Gibbs compression kills the first centered basis vector and retains τ on the second. Thus H=G−Π is a rank-one orthogonal projection with squared Frobenius norm 1 and largest row half-L1 norm 2/3; powers and the upper-endpoint maximum follow, since the positive endpoint has larger modulus. In dimension two the sole centered eigenvalue must be zero. Inspected frozen verify.py and its recorded 3,714 assertion result, without executing the supplied script; finite checks do not establish the uniform inequalities or all-time powers.

## originality

PASS

The distinct claim is the complete sharp attainable interval for the sole potentially nonzero compressed centered mode, with endpoint and positivity statements and exact worst-case errors. Neither the general compression framework nor memory creation by itself is credited as new.

## value

PASS

The natural minimal dimension for a nonreversible obstruction is three. The exact feasible range quantifies how large the all-time deterioration can be after exact mixing, distinguishes negative and positive retained modes, and identifies when strict positivity can be retained. A single counterexample or general nonnormality bound would not supply this sharp benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
