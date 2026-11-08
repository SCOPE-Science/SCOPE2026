# Independent mathematical audit

## correctness

PASS

Logarithmic unitary Uf(s)=exp(-s/2) f(exp(-s)) maps C_alpha to upper Wiener–Hopf convolution Wg(s)=int_0^infty k(t)g(s+t)dt with k=alpha exp(-t/2)(1-exp(-t))^(alpha-1). For every alpha>0 k∈L1 and Hankel H(s,t)=k(s+t) is Hilbert–Schmidt: ∫t|k(t)|²dt<∞ even when alpha<1. Kernel product gives W W* - W* W = H², so the claimed defect is -J_alpha² after inverse unitary. J_alpha(x,y)=alpha(1-xy)^(alpha-1) is trace class by absolutely summable monomial rank-one expansion a_j=alpha(1-alpha)_j/j!, whose trace-norm summands are |a_j|/(2j+1)=O(j^(-alpha-1)). Beta and squared-kernel integrals give trace J=alpha sqrt(pi)Gamma(alpha)/(2Gamma(alpha+1/2)) and ||defect||_1=alpha²(psi(2alpha)+EulerGamma)/(2alpha-1), removable pi²/24 at alpha=1/2. Independently numerically integrated the kernel norm at alpha=1/4,1/2,1,3/2,2 and matched the formula. Integer monomials yield rank m with alternating signs; noninteger tail coefficients share sign (-1)^floor(alpha), with finitely many opposing signs. First-m-moment nullspace is infinite-dimensional definite, while compressed/scaled moment interpolants realize the full finite opposing index; analytic kernel with every a_j nonzero gives injectivity and dense range. This proves all stated parity bands; finite symbolic checks are corroborative, not exhaustive.

## originality

PASS

Comparison across equivalence, broader coverage, exact results and claimed implication finds no decisive existing result that covers the final scoped theorem in accessible inspected material; precise covered ingredients and full-text access risks are explicitly recorded. This is a best-knowledge scientific judgment, not an attestation of independence or a guarantee of historical priority.

## value

PASS

The self-commutator gives a natural measure of nonnormality for an established continuous operator family. Exact trace-class energy and a complete signed Hankel spectral-inertia transition from finite rank at every integer to infinite rank at every other positive order answer structural questions beyond boundedness or generic Wiener–Hopf factorization; individual eigenvalues remain open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
