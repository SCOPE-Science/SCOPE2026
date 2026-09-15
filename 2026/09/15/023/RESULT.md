# Relative Host joining rigidity over the 2-step Host-Kra factor fails for singular-spectrum Z^2-actions

## Context

The admitted target asked whether every pairwise-independent 3-fold self-joining of a free
ergodic measure-preserving Z^2-action with maximal spectral type purely singular on T^2 is
relatively independent over its 2-step Host-Kra-Ziegler factor Z_{<2}, in particular whether
triviality of Z_{<2} would force the joining to be product measure. This connects Host's
1991 pairwise-independent-joining rigidity for weakly mixing 1D singular-spectrum systems,
the pairwise-independently-determined (PID) program, and the Host-Kra-Ziegler distal
structure theory for Z^d-actions.

## Definitions

- (X,B,mu,T): free ergodic measure-preserving Z^2-action; U^{(m,n)} the Koopman operators.
- Maximal spectral type on L^2_0(X,mu) is purely singular: some (hence every) maximal
  spectral type sigma_max on T^2 satisfies sigma_max perpendicular to Lebesgue m_{T^2}.
- Z_{<2}(X,T): 2-step Host-Kra-Ziegler factor, an inverse limit of 2-step nilsystems, with
  Z_{<1} equal to the Kronecker factor.
- 3-fold self-joining lambda on X^3 invariant under diagonal T with all three 2D marginals
  equal to mu x mu (pairwise independent). Relatively independent over Z_{<2} means
  integral of f1 x f2 x f3 d lambda = 0 whenever some f_i in L^infty has E[f_i|Z_{<2}]=0.

## Result (disproof of the main clause)

There exists a free ergodic Z^2-action (X,mu,T) with sigma_max singular on T^2, with
Z_{<2} nontrivial (equal to an irrational-rotation factor), and a pairwise-independent
3-fold self-joining lambda that is not relatively independent over Z_{<2}: there are
f_1,f_2,f_3 in L^infty with E[f_i|Z_{<2}]=0 for all i but integral f_1 x f_2 x f_3 d lambda
= 1. Hence 2D spectral singularity does not imply relative independence over Z_{<2}.
The trivial-Z_{<2} subcase is not addressed by this example and remains open.

## Construction and proof

Let Y={0,1}^Z with fair product measure mu_Y and shift S; Z=T with Lebesgue measure and
irrational rotation Rz=z+alpha. Put X=YxZ, mu=mu_Yxmu_Z, T^{(m,n)}(y,z)=(S^m y,R^n z).

Freeness: for m!=0, Fix(S^m) is finite hence mu_Y-null; for m=0,n!=0 the rotation is
fixed-point-free. Ergodicity: (1,0)-invariance plus ergodicity of S forces any invariant F
to be z-measurable; (0,1)-invariance plus ergodicity of R forces constancy.

Spectral singularity: with orthonormal bases {g_j} of L^2_0(Y) and {e_k}_{k!=0} of L^2_0(Z),
the basis {g_jx1}x{1xe_k}x{g_jxe_k} of L^2_0(X) has every spectral measure supported on the
fixed null set N=T x E, E={k alpha: k in Z} countable, m_{T^2}(N)=0. E.g. g x 1 has
spectral measure sigma^S_g x delta_0. Hence any countable weighted maximal spectral type
lives on N: sigma_max is singular on T^2. The mechanism: one-dimensional Lebesgue
behaviour m_T x delta_0 is singular in two dimensions.

Kronecker factor: Fourier expansion F(y,z)=sum_k g_k(y)e_k(z) plus eigenvalue equation
forces each g_k to be an S-eigenfunction; S (Bernoulli) is weakly mixing, so at most one k
survives and eigenfunctions are z-measurable. Hence Kronecker equals the rotation
coordinate.

Z_{<2}: the relative product X x_Z X ~= YxYxZ with SxSxR is ergodic (SxS ergodic since S is
weakly mixing), so X->Z is relatively weakly mixing. With the admitted premise that
Z_{<2}->Z_{<1}=Kronecker is a distal tower step, the standard Furstenberg-Zimmer fact that
a relatively weakly mixing extension admits no nontrivial intermediate distal extension
forces Z_{<2}=Z. Hence E[g x 1 | Z_{<2}]=(int g) x 1.

Joining: on Y let lambda_Y be the law of (Y_1,Y_2,Y_1+Y_2 mod 2 coordinatewise) with
Y_1,Y_2 i.i.d. ~ mu_Y; each pair of coordinates is independent (map (a,b)->(a,a+b)
preserves fair-coin^2), while g(y)=(-1)^{y_0} satisfies g x g x g = 1 lambda_Y-a.s. Put
lambda=lambda_Y x mu_Z^3 on X^3~=Y^3xZ^3: diagonal-invariant with all 2D marginals
mu_X^2. With f(y,z)=g(y), int g=0 so E[f|Z_{<2}]=0, but the triple integral equals 1.

## Limitations

Relied-upon standard black boxes: weak mixing of Bernoulli shifts (SxS ergodic),
Furstenberg-Zimmer relatively-weakly-mixing-vs-distal dichotomy, and the distal-tower
property of Host-Kra-Ziegler factors. The construction refutes only the main clause
(nontrivial Z_{<2}); the trivial-Z_{<2} implication is explicitly left open. No claim is
made about mixing or higher-order mixing.

## Reproducibility

Analytic proof is self-contained in DRAFT.md. output/artifacts/bernstein_check.py
(seed 20335, N=200000) empirically certifies the finite Bernstein marginal: coordinate
means ~0, all three pairwise grids ~1/4 per cell, triple-product mean exactly 1.0;
re-run returns BERNSTEIN_CHECK_OK.

## References

- B. Host, Mixing of all orders and pairwise independent joinings of systems with singular
  spectrum, Israel J. Math. 76 (1991).
- E. Janvresse, T. de la Rue, A Class of pairwise-independent Joinings, HAL hal-00143357.
- Y. Gutman et al., Almost sure convergence of the multiple ergodic average for certain
  weakly mixing systems, arXiv:1612.02873.
- H. Furstenberg (1967); E. Glasner, Ergodic Theory via Joinings, Ch. 9; B. Host-B. Kra,
  Ann. of Math. 161 (2005); A. Leibman HKZ survey.
