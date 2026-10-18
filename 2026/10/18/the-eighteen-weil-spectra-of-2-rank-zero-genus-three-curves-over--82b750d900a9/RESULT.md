# The eighteen Weil spectra of 2-rank-zero genus-three curves over \(\mathbf F_4\)

## Finding

The 2-rank-zero hyperelliptic genus-three curves over \(\mathbf F_4\) have **exactly eighteen distinct Weil polynomials**, distributed among their **32** arithmetic isomorphism classes with multiplicities: six polynomial types represented by one class each, ten by two classes each, and two by three classes each. Their common Newton polygon has slopes \(1/3\) and \(2/3\), each with multiplicity three, and every curve has Cartier \(a\)-number two. The isomorphism classification and the class count of 32 are earlier results; the specific finite-field Weil-polynomial distribution is the claim here.

With \(q=4\), write \(L_C(T)=1-e_1T+e_2T^2-e_3T^3+4e_2T^4-16e_1T^5+64T^6\). The complete multiplicity table, with triples \((e_1,e_2,e_3)\), is:

| \((e_1,e_2,e_3)\) | Classes | \((e_1,e_2,e_3)\) | Classes |
| --- | ---: | --- | ---: |
| \((-4,8,-12)\) | 1 | \((-4,12,-28)\) | 1 |
| \((-2,0,4)\) | 2 | \((-2,4,-12)\) | 2 |
| \((-2,4,-4)\) | 2 | \((-2,8,-12)\) | 2 |
| \((0,0,-12)\) | 1 | \((0,0,-4)\) | 2 |
| \((0,0,4)\) | 2 | \((0,0,12)\) | 1 |
| \((0,4,-4)\) | 3 | \((0,4,4)\) | 3 |
| \((2,0,-4)\) | 2 | \((2,4,4)\) | 2 |
| \((2,4,12)\) | 2 | \((2,8,12)\) | 2 |
| \((4,8,12)\) | 1 | \((4,12,28)\) | 1 |

The number of rational points is distributed as follows: two classes have one point, eight have three, twelve have five, eight have seven, and two have nine.

## Assumptions and scope

Throughout, \(k=\mathbf F_4=\mathbf F_2(\omega)\), with \(\omega^2+\omega+1=0\). The claim concerns **all** smooth, projective, geometrically connected hyperelliptic genus-three curves over \(k\) with Jacobian \(2\)-rank zero, considered up to \(k\)-isomorphism. A Weil polynomial means the degree-six numerator of the Hasse–Weil zeta function, equivalently the characteristic polynomial of geometric Frobenius written in reciprocal form. Each distinct Weil polynomial is an isogeny type of Jacobians over \(k\), by the standard Tate–Honda isogeny criterion.

## Proof

**Reduction to the whole finite moduli stratum.** In characteristic two, the Deuring–Shafarevich formula for a hyperelliptic Artin–Schreier cover gives \(2\)-rank equal to the number of geometric branch points minus one. Rank zero therefore forces a unique branch point, which is rational over \(k\). Choosing this point as infinity, the cover has an odd-degree polynomial equation. Riemann–Hurwitz makes its pole order seven. Adding \(h(x)^2+h(x)\) removes all positive even powers, and translates the constant into representatives of \(k/\{z^2+z:z\in k\}\). Since \(k^*=\{1,\omega,\omega^2\}\) and seventh powers act bijectively, the leading coefficient can be normalized to one. Thus every such curve has a reduced equation
\[
 y^2+y=x^7+a x^5+b x^3+c x+d,\qquad a,b,c\in k,\ d\in\{0,\omega\}.
\]
There are exactly 128 such reduced equations.

**Arithmetic isomorphisms.** The genus-three hyperelliptic involution is unique, so every isomorphism descends to a fractional-linear transformation on its quotient \(\mathbf P^1\). The unique branch point is infinity, forcing the transformation to be affine \(x\mapsto ux+t\). Keeping the coefficient of \(y\) equal to one forces the scaling of \(y\) to be one, so the leading \(x^7\) coefficient forces \(u^7=1\). Since \(k^*\) has order three, \(u=1\). The remaining transformations are the four translations \(t\in k\), followed by forced Artin–Schreier reduction in \(y\). Under translation the coefficient of \(x^5\) changes from \(a\) to \(a+t^2\); hence the action is free and each orbit contains exactly one representative with \(a=0\). The 32 representatives are precisely the curves
\[
 C_{b,c,d}: y^2+y=x^7+b x^3+c x+d,\quad b,c\in k,\ d\in\{0,\omega\}.
\]
This is the known isomorphism-census ingredient, reproved here for correctness of the zeta table, not asserted as an original classification.

**Exact zeta enumeration.** For \(n=1,2,3\), put \(N_n=\#C_{b,c,d}(\mathbf F_{4^n})\). The unique point at infinity contributes one, and the exact affine count is
\[
 N_n=1+2\sum_{x\in\mathbf F_{4^n}}\mathbf1_{\operatorname{Tr}_{\mathbf F_{4^n}/\mathbf F_2}(x^7+b x^3+c x+d)=0}.
\]
With \(s_n=4^n+1-N_n\), Newton identities give
\[
 e_1=s_1,\quad e_2=(s_1^2-s_2)/2,\quad e_3=(s_1^3-3s_1s_2+2s_3)/6.
\]
The genus-three functional equation gives the remaining coefficients \(4e_2,-16e_1,64\). The attached `verify_classification.py` enumerates all 32 representatives, computes these integers using irreducible finite-field polynomial models, and produces the complete witness table `classification.csv`. The 18 distinct triples and their multiplicities are given above; the program asserts they sum to 32. This is an exhaustive computation because every isomorphism class has a unique listed representative and each finite-field sum explicitly iterates all its elements.

**Common Cartier and Newton data.** For any Artin–Schreier model above, the holomorphic differential basis is \(dx,x\,dx,x^2\,dx\). Its Cartier operator sends \(x\,dx\) to \(dx\) and annihilates the other basis vectors. Thus the Cartier rank is one and \(a(C)=3-1=2\), while its square is zero, agreeing with \(2\)-rank zero. Every computed triple satisfies \(2\mid e_1\), \(4\mid e_2\) and \(v_2(e_3)=2\). From the functional equation, the lower Newton polygon of \(L_C\) has vertices \((0,0),(3,2),(6,6)\) with respect to \(v_2\), so after normalization by \(v_2(4)=2\) its slopes are \(1/3\) repeated three times and \(2/3\) repeated three times. All the distinct Weil polynomials therefore share the same Newton polygon, strengthening the contrast between Newton-stratum and isogeny classification.

## Verification

Run the two self-contained scripts in the same directory with a standard Python 3 interpreter: `python verify_classification.py` followed by `python independent_check.py`. The first proves the four-element translation action through exhaustive group-law checks, enumerates 32 distinct reduced representatives, reconstructs all 18 polynomial triples and their multiplicities, and rewrites the 32-row `classification.csv`. The second uses *different* irreducible polynomials for the three extension fields, different field arithmetic, the conjugate embedding of \(\mathbf F_4\), and direct enumeration of the roots of \(y^2+y=f(x)\) instead of the trace formula. It reproduces \(N_1,N_2,N_3\) and also checks the predicted fourth-extension count \(N_4\) independently over \(\mathbf F_{256}\) for each class. Both passed on the included artifacts; the captured outputs are `verification_primary.txt` and `verification_independent.txt`. The proof does not extrapolate from finite sampling: the mathematical reduction bounds the domain to these 32 models before the exhaustive enumeration.

## Relationship to prior work

Nart and Sadornil (2004) give a general arithmetic isomorphism classification of genus-three hyperelliptic curves in characteristic two. Their general class-count formula implies the 32-class baseline; neither that count nor the normal forms is asserted as new. Nart's later overview explicitly records the known \(q^2\)-stratum count and the genus-three zeta-polynomial question, but does not tabulate the particular 18-polynomial distribution over \(\mathbf F_4\). Duque-Rosero et al. (first public 2024-01-16) classify invariant-theoretic standard forms in genera three and four for odd characteristic \(p>2\), explicitly omitting characteristic two. Blache and Pierre examine quadratic Artin–Schreier curves \(y^2+y=xR(x)\) with additive \(R\), a different special family. The present finding isolates the complete zeta spectrum in the characteristic-two, genus-three, 2-rank-zero arithmetic stratum, rather than claiming new isomorphism counts or an invariant-theory generalization.

## Limitations

The conclusion is confined to characteristic two over the specific field \(\mathbf F_4\), and to the 2-rank-zero hyperelliptic stratum. It does not classify principal polarizations within a fixed isogeny class, endomorphism rings, or all genus-three curves. The 2004 full text of Nart–Sadornil was not accessible in the present literature inspection; therefore a pre-existing finite-field Weil-polynomial table remains a material priority risk. The 18-type classification is a reproducible calculation, not a claim of absolute bibliographic uniqueness or independent certification.

## References

1. E. Nart and D. Sadornil, *Hyperelliptic curves of genus three over finite fields of even characteristic*, Finite Fields Appl. 10 (2004), 198–220; doi:10.1016/j.ffa.2003.08.002.
2. E. Nart, *Genus 3 curves: a world to explore*, lecture notes, accessible transcription: https://www.sambuz.com/doc/genus-3-curves-a-world-to-explore-ppt-presentation-1092629 (sections on characteristic-two classification and zeta functions).
3. J. Duque-Rosero, H. Goodson, E. Lorenzo García, B. Malmskog, R. Scheidler, *On invariants of Artin–Schreier curves*, arXiv:2401.08843v1, first submitted 2024-01-16, https://arxiv.org/html/2401.08843v1.
4. R. Blache and P. Pierre, *Zeta functions of quadratic Artin–Schreier curves in characteristic two*, arXiv:2112.02860v1, https://arxiv.org/html/2112.02860v1.
5. A. M. Ho and R. Pries, *A Mass Formula for Artin–Schreier Curves over Finite Fields*, arXiv:2203.10187, https://arxiv.org/abs/2203.10187.
