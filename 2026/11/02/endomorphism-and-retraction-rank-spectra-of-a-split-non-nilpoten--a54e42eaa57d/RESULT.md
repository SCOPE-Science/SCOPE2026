# Endomorphism and retraction rank spectra of a split non-nilpotent Leibniz family

## Finding

Let \(q\) be any prime power and \(n\ge2\). Put \(r=n-2\) and \(m=n-1\). Consider the left Leibniz algebra
\[
L_n=\mathbb F_q u\oplus\mathbb F_q v\oplus W,
\qquad \dim_{\mathbb F_q}W=r,
\]
whose only nonzero basis bracket is \([v,u]=u\). All endomorphisms below are \(\mathbb F_q\)-linear and bracket preserving. Write \(E_{n,q}(z)\) for the polynomial whose coefficient at \(z^j\) is the number of endomorphisms of linear rank \(j\), and \(J_{n,q}(z)\) for the analogous polynomial restricted to idempotent endomorphisms.

For \(0\le j\le\min(a,b)\), set
\[
R_{a,b}(j)=\binom aj_q\prod_{i=0}^{j-1}(q^b-q^i),\qquad
I_a(j)=\binom aj_q q^{j(a-j)},
\]
where \(\binom aj_q\) is the Gaussian binomial coefficient. Empty products equal one; these quantities are zero outside their stated ranges.

**Theorem.** The complete endomorphism and idempotent-endomorphism rank polynomials are
\[
\boxed{E_{n,q}(z)=2\sum_{j=0}^{m}R_{m,m}(j)z^j
-\sum_{j=0}^{r}R_{r,m}(j)z^j
+(q-1)q^r z^2\sum_{j=0}^{r}R_{r,r}(j)z^j,}
\]
and
\[
\boxed{J_{n,q}(z)=\sum_{j=0}^{m}I_m(j)z^j
+\sum_{j=0}^{r}I_r(j)(q^{2j}-q^j)z^j
+z^2\sum_{j=0}^{r}I_r(j)q^{r-j}z^j.}
\]
In particular,
\[
\boxed{|\operatorname{End}(L_n)|=2q^{(n-1)^2}+(q-2)q^{(n-2)(n-1)},}
\]
and
\[
\boxed{|\operatorname{Aut}(L_n)|=(q-1)q^{n-2}|\operatorname{GL}_{n-2}(\mathbb F_q)|.}
\]

Fix \(q\) and choose an endomorphism uniformly at random. For every fixed integer \(t\ge0\),
\[
\boxed{\lim_{n\to\infty}\Pr\bigl(\operatorname{rank}f=n-1-t\bigr)
=q^{-t^2}\frac{P_q}{P_{q,t}^2},}
\qquad
P_{q,t}=\prod_{i=1}^{t}(1-q^{-i}),\quad
P_q=\prod_{i=1}^{\infty}(1-q^{-i}).
\]
Moreover,
\[
\boxed{\Pr\bigl(f\in\operatorname{Aut}(L_n)\bigr)
\sim\frac{q-1}{2}P_q\,q^{-(n-1)}.}
\]
The rank law converges in total variation, up to an error \(O_q(q^{-(n-1)})\), to the rank distribution of a uniformly random \((n-1)\times(n-1)\) matrix over \(\mathbb F_q\). The theorem for the concrete algebra holds also in characteristic two; the classification of *all* nonnilpotent non-Lie Leibniz algebras with one-dimensional derived ideal as this family is only invoked in odd characteristic.

## Assumptions and scope

The convention is the **left** Leibniz identity \([x,[y,z]]=[[x,y],z]+[y,[x,z]]\). The algebra above satisfies it over every field; its derived ideal is \(\mathbb F_q u\). In odd characteristic, the classification theorem of Di Bartolo, La Rosa, and Mancini shows that every finite-dimensional nonnilpotent non-Lie left Leibniz algebra with a one-dimensional derived ideal is isomorphic to the stated \(L_n\). No characteristic-two classification assertion is made. We count maps rather than conjugacy classes, and rank is ordinary vector-space image dimension. The formulas include \(r=0\), or equivalently \(n=2\).

## Proof

**1. Three disjoint endomorphism strata.** Let \(\alpha(x)\) and \(\beta(x)\) denote the coefficients of \(u\) and \(v\) in \(x\). Then \([x,y]=\beta(x)\alpha(y)u\). Every endomorphism \(f\) sends the derived ideal to itself, so \(f(u)=a u\) for some \(a\in\mathbb F_q\). Write \(\alpha_f=\alpha\circ f\) and \(\beta_f=\beta\circ f\). Bracket preservation is equivalent to the tensor equality
\[
\beta_f\otimes\alpha_f=a\,\beta\otimes\alpha.
\tag{1}
\]
If \(a\ne0\), evaluating (1) first on \((v,u)\), then on \((W,u)\), \((v,v)\), and \((v,W)\), yields \(\beta_f(v)=1\), \(\beta_f(W)=0\), \(\alpha_f(v)=0\), and \(\alpha_f(W)=0\). Consequently these maps, and only these, have the form
\[
f(u)=a u,\qquad f(v)=v+w_0,\qquad f(w)=T(w),
\quad a\in\mathbb F_q^\times,\ w_0\in W,\ T\in\operatorname{End}_{\mathbb F_q}(W).
\tag{2}
\]
If \(a=0\), equation (1) becomes \(\beta_f\otimes\alpha_f=0\). A pure tensor over a field vanishes exactly when at least one factor vanishes. Thus the maps comprise two linear spaces:
\[
\mathcal A=\{f:f(u)=0,\ f(L_n)\subseteq\mathbb F_q u\oplus W\},\quad
\mathcal B=\{f:f(u)=0,\ f(L_n)\subseteq\mathbb F_q v\oplus W\}.
\tag{3}
\]
Their intersection consists of maps killing \(u\) and taking values in \(W\). Each of \(\mathcal A\) and \(\mathcal B\) is naturally the full vector space of linear maps between two \(m\)-dimensional spaces, while the intersection is the space of maps from an \(m\)-dimensional space into an \(r\)-dimensional space. The family (2) is disjoint from their union.

**2. Rank counting and units.** There are \(R_{a,b}(j)\) linear maps of rank \(j\) from a \(b\)-space to an \(a\)-space: select the image as a Gaussian-binomial subspace and then choose a surjection onto it. By inclusion-exclusion in (3), the contribution is \(2R_{m,m}(j)-R_{r,m}(j)\). In (2) the vectors \(f(u)\) and \(f(v)\) are independent modulo \(W\), so \(\operatorname{rank}f=2+\operatorname{rank}T\). The parameters \(a,w_0\) contribute \((q-1)q^r\), proving the formula for \(E_{n,q}\). Evaluation at \(z=1\) gives
\[
2q^{m^2}-q^{rm}+(q-1)q^{r+r^2}
=2q^{m^2}+(q-2)q^{rm},
\]
since \(r+r^2=rm\). The maps in (2) are invertible exactly when \(T\) is invertible, proving the unit count.

**3. Idempotents.** A rank-\(j\) idempotent linear operator on an \(a\)-space corresponds to a choice of a \(j\)-dimensional image and a complementary kernel, giving \(I_a(j)=\binom aj_q q^{j(a-j)}\).

In \(\mathcal B\), an idempotent map is any idempotent operator on \(\mathbb F_q v\oplus W\), extended by killing \(u\). Hence its rank polynomial is \(\sum_j I_m(j)z^j\).

In \(\mathcal A\), write
\[
f(v)=b u+w_0,\qquad f(w)=\ell(w)u+T(w),\quad
b\in\mathbb F_q,\ w_0\in W,\ \ell\in W^*,\ T\in\operatorname{End}(W).
\]
The equation \(f^2=f\) holds precisely when
\[
T^2=T,\qquad \ell T=\ell,\qquad Tw_0=w_0,\qquad b=\ell(w_0).
\tag{4}
\]
If \(T\) has rank \(j\), the functional \(\ell\) factors through \(\operatorname{im}T\) and has \(q^j\) choices, while \(w_0\in\operatorname{im}T\) has \(q^j\) choices. Condition (4) fixes \(b\). The image of \(f\) is the graph of \(\ell\) on \(\operatorname{im}T\), so its rank is exactly \(j\). This yields \(I_r(j)q^{2j}\) idempotents in \(\mathcal A\).

An idempotent in \(\mathcal A\cap\mathcal B\) has \(\ell=0\), so for each rank-\(j\) projection \(T\), there are exactly \(q^j\) choices of \(w_0\) and its rank is \(j\). Inclusion-exclusion contributes \(I_r(j)(q^{2j}-q^j)\) beyond the \(\mathcal B\) contribution.

Finally, a map in (2) is idempotent precisely when \(a=1\), \(T^2=T\), and \(Tw_0=0\). For a rank-\(j\) projection \(T\), there are \(q^{r-j}\) possible \(w_0\in\ker T\), and the resulting map has rank \(j+2\). This gives the last sum in \(J_{n,q}\) and finishes both enumerations.

**4. Limiting rank law.** Both linear spaces in (3) have \(q^{m^2}\) elements, and each has the rank distribution of a uniform random \(m\times m\) matrix. The intersection has \(q^{rm}\) elements and the disjoint family (2) has \((q-1)q^{rm}\) elements. Thus, for every rank event, the difference between its probability under a uniform Leibniz endomorphism and the corresponding event for a uniform \(m\times m\) matrix is bounded by a constant (depending only on \(q\)) times \(q^{-m}\). This bound is uniform in the event, establishing the claimed total-variation estimate.

For a random \(m\times m\) matrix, the exact probability of nullity \(t\) is
\[
q^{-t^2}\frac{\displaystyle\prod_{i=t+1}^{m}(1-q^{-i})^2}
{\displaystyle\prod_{i=1}^{m-t}(1-q^{-i})}
\qquad(0\le t\le m).
\]
Taking \(m\to\infty\) proves the pointwise limit; it is a probability distribution because it is the limiting distribution of square-matrix nullity and the omitted tail is uniformly summable (the displayed expression is at most \(q^{-t^2}/P_q\)). The unit formula gives
\[
\frac{|\operatorname{Aut}(L_n)|}{|\operatorname{End}(L_n)|}
=\frac{(q-1)q^{r^2+r}\prod_{i=1}^{r}(1-q^{-i})}
{2q^{(r+1)^2}+(q-2)q^{r(r+1)}}
\sim\frac{q-1}{2}P_q\,q^{-(r+1)},
\]
concluding the theorem.

## Verification

The accompanying `verify.py` enumerates all \(q^{n^2}\) linear maps as candidate matrices over prime fields, independently checks all basis bracket relations and the equation \(f^2=f\), and compares both rank distributions with the claimed formulas. Its six exhaustive test cases are \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\); the corresponding counts include
\[
E_{3,3}(z)=1+56z+102z^2+12z^3,\quad
J_{3,3}(z)=1+18z+4z^2+z^3,
\]
\[
E_{4,2}(z)=1+77z+550z^2+372z^3+24z^4,\quad
J_{4,2}(z)=1+40z+44z^2+13z^3+z^4.
\]
Thirty additional symbolic consistency checks use the formula at finite prime-power field orders, but they are not exhaustive matrix searches at those sizes. Execute `python verify.py` using Python 3 (no third-party packages). The proof, rather than the finite computation, establishes the formulas for all \(n,q\).

## Relationship to prior work

Di Bartolo, La Rosa, and Mancini's 2023 preprint (Theorem 2.2) classifies the nonnilpotent non-Lie derived-one-dimensional Leibniz algebras in characteristic different from two. Their Theorem 2.4(ii) gives the automorphism block matrices. Those results motivate the present investigation, but their derivation/automorphism/biderivation treatment does not enumerate all noninvertible endomorphisms, idempotent retractions, rank distributions, or the finite-field limiting corank law. Standard Gaussian coefficients and random-matrix nullity counts are ingredients here, not asserted discoveries. Kurdachenko, Subbotin, and Yashchuk study endomorphisms of **infinite-dimensional cyclic** Leibniz algebras, not the finite-dimensional family here. Nearby publications about free metabelian Leibniz algebra orbit-preserving endomorphisms concern different algebras and different invariants.

## Limitations

The formulas treat the fixed explicit algebra, not all Leibniz algebras of a given dimension in characteristic two. The limiting law fixes the field order and sends the dimension to infinity; it does not assert simultaneous uniformity in both parameters. Enumeration uses labeled endomorphisms, not conjugacy or isomorphism types. Exhaustive verification covers only the six explicitly stated finite configurations. A mathematically equivalent enumeration under alternative terminology could exist in uninspected literature, especially in older work on finite-algebra endomorphism monoids; no claim of a literature-exhaustive novelty proof is made.

## References

- A. Di Bartolo, G. La Rosa, and M. Mancini, *Non-nilpotent Leibniz algebras with one-dimensional derived subalgebra*, first public version 2023-07-18, arXiv:2307.09102, https://arxiv.org/abs/2307.09102; especially Theorems 2.2 and 2.4.
- L. A. Kurdachenko, I. Ya. Subbotin, and V. S. Yashchuk, *On the endomorphisms and derivations of some Leibniz algebras*, 2021, arXiv:2104.05922, https://arxiv.org/abs/2104.05922 (infinite-dimensional cyclic case).
- T. Adiyaman Taş and Z. Özkurt, *Endomorphisms which preserve orbits of free metabelian Leibniz algebras*, *Communications in Algebra* 52 (2024), 566–571, https://doi.org/10.1080/00927872.2023.2245888 (different free-algebra setting).
