# Pure-power rigidity and a sharp gap for two-coordinate cap concentration in complex Hardy spaces

## Finding

Let \(n\ge3\), \(d\ge2\) be integers, and \(0<t<1\). Give the complex unit sphere \(S^{2n-1}\subset\mathbb C^n\) probability surface measure \(\sigma\). Let \(\mathcal H_d\) be the complex vector space of holomorphic homogeneous polynomials of degree exactly \(d\), with norm \(\|P\|_2^2=\int_{S^{2n-1}}|P|^2\,d\sigma\). Consider the union of coordinate caps
\[
 E_t=\{z\in S^{2n-1}:|z_1|^2>t\ \text{or}\ |z_2|^2>t\}.
\]
Write \(\Pi_d\) for the orthogonal projection in \(\mathcal H_d\) onto \(\operatorname{span}\{z_1^d,z_2^d\}\). Define \(\lambda_{a,b}=\int_{E_t}|z_1|^{2a}|z_2|^{2b}|z_3|^{2(d-a-b)}\,d\sigma/\int_{S^{2n-1}}|z_1|^{2a}|z_2|^{2b}|z_3|^{2(d-a-b)}\,d\sigma\) for \(a,b\ge0\), \(a+b\le d\); these depend only on \(a,b,n,d,t\), not on the allocation of remaining degree among coordinates 3 through \(n\).

**Theorem.** The two largest distinct eigenvalues of the restriction/concentration operator on \(\mathcal H_d\) are exactly
\[
 \Lambda=\lambda_{d,0}=\lambda_{0,d},\qquad
 \Lambda_2=\lambda_{d-1,1}=\lambda_{1,d-1}<\Lambda.
\]
The top eigenspace is precisely \(\operatorname{span}\{z_1^d,z_2^d\}\). For \(d>2\), the second eigenspace is \(\operatorname{span}\{z_1^{d-1}z_2,z_1z_2^{d-1}\}\); for \(d=2\), it is \(\operatorname{span}\{z_1z_2\}\). Thus all sharp equality cases in \(\int_{E_t}|P|^2\,d\sigma\le\Lambda\|P\|_2^2\) are the nonzero polynomials \(P=A z_1^d+B z_2^d\).

The **exact sharp spectral gap** is the following strictly positive elementary integral, with \(B\) the Euler beta function:
\[
 \boxed{\Delta_{n,d}(t)=\Lambda-\Lambda_2
 =\frac{d+1}{B(d+2,n-2)}\int_t^{\min(2t,1)}
 t(s-t)\big[t^{d-1}-(s-t)^{d-1}\big](1-s)^{n-3}\,ds>0.}
\]
In particular the sharp stability inequality for all complex \(P\in\mathcal H_d\) is
\[
 \int_{E_t}|P|^2\,d\sigma\le\Lambda\|P\|_2^2
 -\Delta_{n,d}(t)\|P-\Pi_dP\|_2^2.
\]
No larger coefficient than \(\Delta_{n,d}(t)\) works, as witnessed by a second-eigenvalue monomial.

## Assumptions and scope

Coordinates are complex, the sphere measure is probability normalized, and degree is **exactly** \(d\), not degree at most \(d\). The result concerns holomorphic polynomials (equivalently, symmetric holomorphic tensors); it is not a statement about all real spherical harmonics. The two caps have the same squared-modulus threshold and lie in two orthogonal complex coordinate directions. Boundary inequalities are unchanged because the cap boundaries have measure zero. The theorem holds for all integers \(n\ge3,d\ge2\) and all real \(0<t<1\).

More generally, for a multi-index \(\alpha\in\mathbb N_0^n\) with \(|\alpha|=d\), set \(a=\alpha_1,b=\alpha_2\), \(N=n+d\), and \(c=N-a-b-2\ge1\). In the orthogonal monomial basis the full spectrum, including multiplicities, is given by the eigenvalue \(\lambda_{a,b}\) with \(\alpha_3+\cdots+\alpha_n=d-a-b\). Its multiplicity for each ordered pair \((a,b)\) is \(\binom{n+d-a-b-3}{n-3}\); equal numerical eigenvalues from different ordered pairs have combined multiplicity. This determines the complete finite spectrum without claiming all non-top eigenvalues are distinct.

The exact scalar eigenvalues are elementary. If \(t\ge\tfrac12\),
\[
 \lambda_{a,b}=\sum_{j=0}^a\binom{N-1}{j}t^j(1-t)^{N-1-j}
 +\sum_{j=0}^b\binom{N-1}{j}t^j(1-t)^{N-1-j}.
\]
If \(0<t\le\tfrac12\), put \(C=(N-1)!/[a!b!(c-1)!]\); then
\[
 \lambda_{a,b}=1-C\sum_{j=0}^{c-1}(-1)^j\binom{c-1}{j}t^{a+b+j+2}
 \sum_{r=0}^j\frac{\binom jr}{(a+r+1)(b+j-r+1)}.
\]
The two expressions coincide at the common boundary. These formulas make both sharp constants exactly computable with rational arithmetic for rational \(t\).

## Proof

**1. Orthogonal diagonalization and Dirichlet law.** Independent coordinate phase rotations preserve both \(E_t\) and \(\sigma\), so different holomorphic monomials are orthogonal on both the whole sphere and \(E_t\). For \(|\alpha|=d\),
\[
 \int_{S^{2n-1}}|z^\alpha|^2\,d\sigma
 =\frac{(n-1)!\prod_{j=1}^n\alpha_j!}{(n+d-1)!}.
\]
Under the probability measure proportional to \(|z^\alpha|^2d\sigma\), the vector \((|z_1|^2,\dots,|z_n|^2)\) has Dirichlet parameters \((\alpha_1+1,\dots,\alpha_n+1)\). Its first two coordinates have density
\[
 f_{a,b}(x,y)=\frac{(N-1)!}{a!b!(c-1)!}x^ay^b(1-x-y)^{c-1}
 \quad(x,y>0,\ x+y<1).
\]
Therefore \(\lambda_{a,b}=\Pr\{X_1>t\text{ or }X_2>t\}\). Integrating the complement square for \(2t\le1\) gives the stated finite polynomial; for \(2t\ge1\) the two cap events are disjoint and their beta-binomial tails give the second expression.

**2. Strict transfer from unused coordinates.** Suppose \(\alpha_j\ge1\) for some \(j\ge3\). Transfer one unit of exponent from \(\alpha_j\) to either \(\alpha_1\) or \(\alpha_2\). Condition on \(X_1+X_j\) and the other coordinates. Before the transfer the split fraction has law \(\mathrm{Beta}(\alpha_1+1,\alpha_j+1)\); afterwards it has law \(\mathrm{Beta}(\alpha_1+2,\alpha_j)\). The new density divided by the old is a positive constant times \(u/(1-u)\), which is strictly increasing. Hence the new \(X_1\) stochastically increases conditionally, leaving \(X_2\) unchanged. Since \(\{X_1>t\text{ or }X_2>t\}\) is increasing in \(X_1\), concentration strictly increases. Strictness follows because the Dirichlet density is positive on the simplex interior and there is an open set with \(X_2<t\) where \(X_1\) crosses \(t\). The same argument holds for transferring to the second coordinate.

**3. Strict imbalance ordering when all degree lies in the first two coordinates.** For \(a+b=d\), let \(S=X_1+X_2\), \(U=X_1/S\). The variables are independent, with \(S\sim\mathrm{Beta}(d+2,n-2)\) and \(U\sim\mathrm{Beta}(a+1,b+1)\). Write \(V=|U-\tfrac12|\) and \(\delta=|a-b|/2\). For \(0<v<\tfrac12\), the density of \(V\) is proportional to
\[
 \big(\tfrac14-v^2\big)^{d/2}
 \cosh\!\left(\delta\log\frac{\frac12+v}{\frac12-v}\right).
\]
For \(\delta_2>\delta_1\ge0\), the ratio of these densities increases strictly with \(v\): differentiating its logarithm in the positive log-odds variable gives \(\delta_2\tanh(\delta_2 h)-\delta_1\tanh(\delta_1 h)>0\), since \(x\mapsto x\tanh(xh)\) increases for \(x\ge0\). Consequently \(V\) is strictly stochastically larger as \(|a-b|\) increases. Conditional on \(S=s\), the cap union holds automatically when \(s>2t\), never when \(s\le t\), and for \(t<s<\min(2t,1)\) it is exactly the strict tail event \(V>t/s-\tfrac12\). This interval has positive beta mass for each \(0<t<1\), giving strict increase of \(\lambda_{a,d-a}\) with \(|2a-d|\).

**4. Exact first two spectral levels.** By repeated strict transfers, every monomial using an outside coordinate is improved by assigning its degree to the first two coordinates. By Step 3, the only highest full-allocation pairs are \((d,0)\) and \((0,d)\); the next pairs are \((d-1,1)\) and \((1,d-1)\). Every monomial outside those pairs has concentration at most the latter: if both cap exponents are positive, transfer all outside degree to a cap coordinate and use Step 3; if exactly one or neither is positive, first transfer one outside unit to the missing cap coordinate and all remaining outside degree to the other, obtaining \((d-1,1)\) or its reversal. At least one transfer is strict whenever the monomial has outside degree. The only equal second-level pairs are therefore the stated ones.

**5. Exact gap.** Relative to the conditional \(S\), the two competing split laws are \(U\sim\mathrm{Beta}(d+1,1)\) and \(U\sim\mathrm{Beta}(d,2)\). For \(r=t/s\in(\tfrac12,1)\), the difference of their outside-central-interval probabilities is
\[
 (d+1)r(1-r)\big[r^{d-1}-(1-r)^{d-1}\big].
\]
The density of \(S\) is \(s^{d+1}(1-s)^{n-3}/B(d+2,n-2)\). Integrating over \(t<s<\min(2t,1)\) and simplifying gives exactly \(\Delta_{n,d}(t)\). Its integrand is strictly positive except at endpoints. Diagonality then proves the full sharp stability inequality and its equality/optimality assertions.

## Verification

The accompanying self-contained `verify.py` uses only Python's standard library and exact rational arithmetic. Run `python verify.py`. It evaluates both polynomial branches of every relevant eigenvalue, compares every monomial branch with the predicted first and second levels, and reconstructs the sharp gap independently by integrating its polynomial integrand termwise. The recorded result is **5,208 exact rational assertions passed** for \(n=3,\dots,7\), \(d=2,\dots,8\), six rational thresholds spanning both sides of \(1/2\), and separate degree-one boundary checks. These finite tests are not a proof of the universal assertions, which are established by the preceding likelihood-ratio arguments.

## Relationship to prior work

Separately radial/quasi-elliptic Toeplitz compression and diagonalization on complex balls are established methods; see Quiroga-Barranco (2015, 2021), and Bauer–Hagger–Vasilevski (2019). The preceding methods provide monomial integral representations but do not themselves give the ordered top two eigenvalues, the strictly positive all-degree spectral gap, or the complete sharp optimizer classification for this two-cap union. Here the crucial extra input is the strict likelihood-ratio order of symmetrized beta split distributions, combined with a transfer principle. An unindexed exact equivalent in the specialized Toeplitz/toric literature has not been ruled out.

## Limitations

The geometry is restricted to a union of **two equal-threshold orthogonal coordinate caps**; no corresponding claim is made for three or more caps, unequal thresholds, arbitrary cap axes, or nonholomorphic harmonic spaces. The spectral-order assertions do not claim the complete ordering of every lower eigenvalue. Independent mathematical audit and comprehensive bibliographic exhaustiveness remain outstanding.

## References

1. R. Quiroga-Barranco, *Toeplitz operators, \(\mathbb T^m\)-invariance and quasi-homogeneous symbols*, arXiv:2106.01980, first posted 2021-06-03. Sections 1, 4, and 7.
2. R. Quiroga-Barranco, *Separately Radial and Radial Toeplitz Operators on the Unit Ball and Representation Theory*, arXiv:1509.07063 (2015), especially Section 5.
3. W. Bauer, R. Hagger, N. Vasilevski, *Algebras of Toeplitz operators on the \(n\)-dimensional unit ball*, Complex Analysis and Operator Theory **13** (2019), 493–524; DOI: 10.1007/s11785-018-0837-y.
