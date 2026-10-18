# Anisotropy-invariant Walsh projection constants in Lipschitz cubes

## Finding

Fix an integer \(n\geq 2\) and arbitrary positive real weights \(w_1,\ldots,w_n\). Equip \(X=\{-1,1\}^{n}\) with the weighted Hamming metric
\[
d_w(x,y)=\sum_{i=1}^{n}w_i\mathbf{1}_{x_i\neq y_i}.
\]
Let \(o=(1,\ldots,1)\), and let \(\operatorname{Lip}_0(X,d_w)\) be the real Banach space of functions vanishing at \(o\), with the Lipschitz norm. For \(S\subseteq[n]\), put \(\chi_S(x)=\prod_{i\in S}x_i\).

Let \(\varnothing\neq\mathcal A\subseteq 2^{[n]}\setminus\{\varnothing\}\) be invariant under some **transitive permutation subgroup** of \(S_n\), and set
\[
E_{\mathcal A}=\operatorname{span}\{\chi_S-1:S\in\mathcal A\}\subset\operatorname{Lip}_0(X,d_w).
\]
Then the **least norm of any real linear projection** onto this spectral subspace is
\[
\boxed{\lambda(E_{\mathcal A},\operatorname{Lip}_0(X,d_w))
=\frac1{2^{n-1}}\sum_{z\in\{-1,1\}^{n-1}}
\left|\sum_{\substack{S\in\mathcal A\\1\in S}}
\prod_{j\in S\setminus\{1\}}z_{j-1}\right|.}
\]
The normalized Walsh Fourier projection attains the infimum. In particular **the answer is independent of all positive edge weights**, even if their ratios are arbitrarily large.

For the homogeneous Walsh layer \(\mathcal A=\{S\subseteq[n]:|S|=d\}\), \(1\leq d\leq n\), the exact value is the finite Krawtchouk sum
\[
\boxed{\lambda_{n,d}=
\frac1{2^{n-1}}\sum_{k=0}^{n-1}\binom{n-1}{k}
\left|\sum_{j=0}^{d-1}(-1)^j\binom{k}{j}
\binom{n-1-k}{d-1-j}\right|,}
\]
with binomial coefficients outside their natural range defined to be zero. At quadratic degree it specializes to
\[
\lambda_{n,2}=
\frac{n-1}{2^{n-2}}\binom{n-2}{\lfloor(n-2)/2\rfloor}.
\]
Thus every positive weighting of the four-dimensional cube gives the exact quadratic-layer projection constant \(3/2\). The weight-insensitivity also applies to spectral supports invariant only under a proper transitive subgroup, not necessarily under the whole symmetric group.

## Assumptions and scope

All functions and projections are real-linear and real-valued. The cube is finite, each weight is strictly positive, and all nonempty spectral sets are excluded from the constant character. The transitive group acts **on the index family** \(\mathcal A\); it is *not* asserted to act isometrically on the anisotropically weighted metric. Translation by coordinatewise sign multiplication, unlike coordinate permutation, is always a metric isometry. The projection constant is relative to the stated ambient Lipschitz space, not the absolute projection constant among arbitrary superspaces.

For a general nontransitive spectral support one still has the coordinate bounds derived in the proof; the weight-independent equality is asserted only under the stated transitivity hypothesis. No infinite-dimensional or non-Hamming metric statement is claimed.

## Proof

**1. Fourier projection and least-norm reduction.** On \(X\), let \(\widehat f(S)=2^{-n}\sum_{x\in X}f(x)\chi_S(x)\). Define
\[
Q_{\mathcal A}f(x)=\sum_{S\in\mathcal A}\widehat f(S)(\chi_S(x)-1).
\]
This is a projection onto \(E_{\mathcal A}\). Let \(G=\{-1,1\}^n\) act on the pointed Lipschitz space through the linear isometries \((U_a f)(x)=f(ax)-f(ao)\), where multiplication is coordinatewise. Because \(U_a(\chi_S-1)=\chi_S(a)(\chi_S-1)\), \(E_{\mathcal A}\) is invariant. Given any projection \(P\) onto that space, averaging \(U_a^{-1}PU_a\) over \(G\) does not increase its norm and yields an equivariant projection. Distinct nonconstant Walsh characters give the distinct one-dimensional eigenspaces of this action on the space of functions modulo constants. Hence the only equivariant projection onto \(E_{\mathcal A}\) is \(Q_{\mathcal A}\). Therefore
\[
\lambda(E_{\mathcal A},\operatorname{Lip}_0(X,d_w))=\|Q_{\mathcal A}\|.
\]

**2. The directional upper bound.** Write \(x^{(i)}\) for \(x\) with its \(i\)-th sign flipped. The weighted path metric yields exactly
\[
\|f\|_{\mathrm{Lip}}=\max_{i,x}\frac{|f(x)-f(x^{(i)})|}{w_i}.
\]
Fix \(i\). For \(z\in\{-1,1\}^{n-1}\), define the signed coordinate derivative
\[
g_i(z)=\tfrac12\big(f(x_i=1,z)-f(x_i=-1,z)\big).
\]
If \(\|f\|_{\mathrm{Lip}}\leq1\), then \(\|g_i\|_{\infty}\leq w_i/2\). Define the *directional Walsh kernel*
\[
K_i(z)=\sum_{\substack{S\in\mathcal A\\i\in S}}\chi_{S\setminus\{i\}}(z),
\qquad c_i=2^{-(n-1)}\sum_z|K_i(z)|.
\]
The Fourier coefficient of \(f\) at \(S\ni i\) is exactly the Fourier coefficient of \(g_i\) at \(S\setminus\{i\}\). Consequently the \(i\)-th directional derivative of \(Q_{\mathcal A}f\) is convolution of \(g_i\) with \(K_i\). For every value of the other coordinates its absolute value is at most \((w_i/2)c_i\). The corresponding edge difference is twice this derivative, so
\[
\boxed{\|Q_{\mathcal A}\|\leq\max_{1\leq i\leq n}c_i.}
\]
This inequality holds even when \(\mathcal A\) is not coordinate-transitive.

**3. A compatible sharp sign-gradient.** Choose \(i\) minimizing the positive weights, and fix a sign function \(h(z)\in\{-1,1\}\) such that \(h(z)K_i(z)=|K_i(z)|\) (choose either sign when the kernel vanishes). Define, up to subtracting its value at \(o\),
\[
f(x)=\tfrac{w_i}{2}x_i h(x_{[n]\setminus\{i\}}).
\]
Flipping coordinate \(i\) changes \(f\) by exactly \(w_i\); flipping another coordinate \(j\) changes it by at most \(w_i\leq w_j\). Thus \(\|f\|_{\mathrm{Lip}}=1\) for **every** positive weight vector with \(w_i\) minimal. Evaluate the \(i\)-directional derivative of \(Q_{\mathcal A}f\) at the all-positive vertex. Its magnitude is
\[
\frac{w_i}{2}\,2^{-(n-1)}\sum_z h(z)K_i(z)
=\frac{w_i}{2}c_i.
\]
Therefore \(\|Q_{\mathcal A}\|\geq c_i\). This proves the useful coordinate-shadow fact that equality with \(\max_jc_j\) holds whenever a least-weight coordinate also maximizes \(c_j\).

**4. Transitive support makes all shadows equal.** Permuting coordinates by a subgroup preserving \(\mathcal A\) carries \(K_i\) to \(K_j\) for any coordinates in the same orbit and preserves uniform counting measure. Under transitivity, all \(c_i\) coincide. Whichever coordinate minimizes the weights therefore attains the common maximum. Combining the preceding two steps proves the boxed exact formula and its complete weight independence.

**5. Homogeneous layers.** When \(\mathcal A\) contains every subset of size \(d\), the kernel \(K_i\) is the sum of all \((d-1)\)-fold Walsh products on \(n-1\) signs. If exactly \(k\) of these signs are negative, expand the products by choosing \(j\) negative and \(d-1-j\) positive coordinates. There are \(\binom{k}{j}\binom{n-1-k}{d-1-j}\) such products, each with sign \((-1)^j\). Averaging their absolute sum over the \(\binom{n-1}{k}\) sign patterns proves the finite formula. For \(d=2\), this is the expected absolute value of a sum of \(n-1\) independent signs; evaluating the elementary binomial sum gives the displayed closed form. All boundary values \(d=1\) and \(d=n\) equal one.

## Verification

The standalone standard-library program `CHECKER.py` computes Walsh transforms with integer arithmetic and evaluates Lipschitz seminorms using exact rational fractions. Its deterministic tests cover all homogeneous layers in dimensions \(2\) through \(6\), unions of complete levels, a proper-transitive-support example from a six-vertex cubic graph, and strongly unequal positive coordinate weights. For each case it constructs the kernel-sign witness, applies the *actual* finite Fourier projection, checks every weighted edge, and verifies the exact norm ratio. It separately compares the Krawtchouk binomial expression with direct kernels through dimension \(7\), and checks the quadratic identity through dimension \(11\). Run `python CHECKER.py` with Python 3 and no third-party dependencies.

These finite checks verify the implementation and selected instances; the proof above, not the finite enumeration, establishes the universal quantifiers in dimension, support and weights.

## Relationship to prior work

Defant, Galicer, Mansilla, Mastyło and Muro [1] study Walsh spectral subspaces equipped with the **supremum norm**, establishing Fourier projection constants and Krawtchouk-type formulas. Their Theorem 3.1 does not compute the norm of Fourier projections on anisotropically weighted *Lipschitz* spaces. Cúth and Doucha [2] establish projection methods associated with group actions on Lipschitz and Lipschitz-free spaces, especially projection onto orbit-invariant function spaces; those fixed-point ranges are not arbitrary nonconstant Walsh spectral subspaces and their results do not give the sharp formula here.

The specific new information is the exact invariance under **arbitrary positive coordinate weights** and the compatible extremizing sign-gradient despite the loss of coordinate-permutation metric isometries. The basic Fourier averaging method and the unweighted Fourier/Krawtchouk ingredients are not claimed as new. The theorem does not purport to classify spectral supports without transitivity.

## Limitations

The conclusion covers finite weighted Hamming cubes, real scalars, and support families that are invariant under a transitive coordinate group. It is a *relative* projection constant. The directional upper bound remains valid without transitivity but need not be sharp for every nontransitive support and every weight vector. No statement about general metric products, absolute Banach-space projection constants, or dimensions tending to infinity without a specified family is made. The exact formulas are analytically proved; external independent validation has not been performed.

## References

[1] A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, first public version 1 February 2023; specifically Introduction and Theorem 3.1 (the supremum-norm setting).

[2] M. Cúth, M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519, first public version 23 April 2021; specifically Sections 3 and 4 (group-action projections and orbit-invariant functions).
