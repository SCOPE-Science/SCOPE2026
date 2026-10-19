# Exact three-pulse phase feasibility in the ternary ghost-pulse constraint

## Finding

Consider a finite optical word of length \(n\ge 3\) with precisely three occupied positions \(S=\{a,b,c\}\subseteq\{0,\ldots,n-1\}\), where \(a<b<c\). An assignment of a sign \(+1\) or \(-1\) to each occupied position is **ghost-pulse admissible** if, whenever three (not necessarily distinct) occupied indices \(i,j,k\) have the same sign, the position \(i+j-k\), if in the interval \(\{0,\ldots,n-1\}\), is occupied. The unoccupied positions have symbol \(0\). This is the finite, unbounded-interaction ternary ghost-pulse (TGP) constraint of Kashyap, Siegel, and Vardy [1].

**Theorem.** The support \(S\) admits such a phase assignment if and only if at least one of the following holds:

\[
\begin{aligned}
&\text{(outer pair)} &&c>2a\quad\text{and}\quad 2c-a\ge n;\\
&\text{(left pair)} &&b>2a\quad\text{and}\quad\bigl(c=2b-a\ \text{or}\ 2b-a\ge n\bigr);\\
&\text{(right pair)}&&2c-b\ge n\quad\text{and}\quad\bigl(a=2b-c\ \text{or}\ c>2b\bigr).
\end{aligned}
\]

Every qualifying support either satisfies the outer-pair condition or belongs to one of **two disjoint exceptional classes of three-term arithmetic progressions**, exchanged by reflection. The left exceptional class consists precisely of

\[
S=\{a,a+d,a+2d\},\quad d\ge1,\quad 0\le a<d,\quad a+4d<n.
\]

The other exceptional class is its reflected image under \(i\mapsto n-1-i\).

Let \(G_3(n)\) be the number of three-occupied-position binary supports admitting an admissible TGP sign assignment. Define

\[
L_a=\max\left\{2a+1,\left\lceil\frac{n+a}{2}\right\rceil\right\},\qquad
P(n)=\sum_{a=0}^{\lfloor(n-2)/2\rfloor}\frac{(n-L_a)(n+L_a-2a-3)}{2},
\]

and

\[
E(n)=\sum_{d=1}^{\lfloor(n-1)/4\rfloor}\min\{d,n-4d\}.
\]

Then the exact enumerator for **every** \(n\ge3\) is

\[
\boxed{G_3(n)=P(n)+2E(n).}
\]

In particular, the limiting fraction of phase-admissible supports among all three-occupied-position words is

\[
\boxed{\lim_{n\to\infty}\frac{G_3(n)}{\binom n3}=\frac{11}{18}.}
\]

The first values, for \(n=3,\ldots,14\), are \(1,4,10,18,28,44,63,92,120,158,202,258\), respectively. The first two pulse counts impose no obstructions, so weight three is the first nontrivial pulse-number layer for phase feasibility.

## Assumptions and scope

All indices are zero-based. Reflection about the center of the finite interval is permitted, but periodic wrap-around is **not** used. Triples of equal-phase pulses may repeat indices; the requirement is checked only when the generated index lies in the finite interval. Feasibility refers to the **existence** of an assignment of signs to the three occupied slots, not the number of such assignments or to the entire set of unconstrained-density codewords. Binary support words are distinguished by their occupied-position sets. The established formulas apply for every integer \(n\ge3\) and no larger pulse count is claimed.

## Proof

**1. Pair criterion.** For any occupied pair \(u<v\), give these two pulses the same sign and the third pulse the opposite sign. Every monochromatic ordered triple then uses only \(u\) and \(v\). Its generated index lies in \(\{u,v,2u-v,2v-u\}\). The first two positions are already occupied, so the assignment is admissible precisely when each reflected index \(2u-v\) and \(2v-u\) is either outside the interval or belongs to \(S\). Conversely, any admissible signing of three pulses either has a unique equal-sign pair or has all signs equal. In the latter case, changing the third pulse to the opposite sign cannot introduce a new monochromatic triple. Thus, **some admissible signing exists if and only if at least one of the three pairs meets the two-reflection test**.

**2. Explicit criterion.** For the extreme pair \(a,c\), both reflected indices lie strictly beyond the extreme occupied positions. Therefore the pair works precisely when \(2a-c<0\) and \(2c-a\ge n\). For \(a,b\), the left reflection must be negative, while the right reflection is either \(c\) or beyond the interval. For \(b,c\), the right reflection must be at least \(n\), while the left reflection is either \(a\) or negative. These are exactly the three displayed conditions.

**3. The only exceptions to extreme-pair feasibility.** If the pair \(a,b\) works by virtue of \(2b-a\ge n\), then \(c>b>2a\) and \(2c-a>2b-a\ge n\), so the outer pair works too. Otherwise, the pair \(a,b\) requires \(c=2b-a\). Put \(d=b-a\). Its left reflection condition is \(a<d\); its failure to satisfy the outer condition is equivalent to \(a+4d<n\). These are precisely the left exceptional progressions. Similarly, if \(b,c\) works because \(2b-c<0\), then the outer pair also works. Otherwise \(a=2b-c\), and reflection of the interval maps the resulting exception bijectively onto the left exceptional class. The two exceptional classes cannot overlap: the left one has \(a<d\), while its reflected right counterpart has \(a\ge2d\), in the same progression notation.

**4. Exact enumeration.** For fixed outer endpoints \(a<c\) satisfying the outer-pair test, the middle position has exactly \(c-a-1\) choices. The lower bound on \(c\) is \(L_a\), and an admissible outer pair requires \(a\le\lfloor(n-2)/2\rfloor\). Summing the resulting arithmetic progression in \(c\) gives \(P(n)\). For a left exceptional progression with step \(d\), the starting point may be any integer \(a\) with \(0\le a\le\min\{d-1,n-1-4d\}\). There are \(\min\{d,n-4d\}\) such choices. Summing gives \(E(n)\), and reflection doubles this count without overlap. Thus \(G_3(n)=P(n)+2E(n)\) exactly.

For an alternative constant-time evaluation of the exceptional term, let \(u=\lfloor n/5\rfloor\) and \(v=\lfloor(n-1)/4\rfloor\). Splitting at \(5d\le n\) gives

\[
2E(n)=5u(u+1)-4v(v+1)+2n(v-u).
\]

For the main term, split the outer-endpoint sum at \(3a+2<n\), where \(L_a=\lceil(n+a)/2\rceil\), and use \(L_a=2a+1\) thereafter. Summing separately over the two parities of \(a\) yields the following cubic polynomials for \(108P(n)\), according to \(n\bmod6\):

| Remainder | \(108P(n)\) |
|---|---|
| \(0\) | \(n^2(11n-18)\) |
| \(1\) | \((n-1)(11n^2-7n-22)\) |
| \(2\) | \((n-2)(11n^2+4n+20)\) |
| \(3\) | \(11n^3-18n^2-27n+54\) |
| \(4\) | \(11n^3-18n^2+12n-32\) |
| \(5\) | \((n-2)(n+1)(11n-7)\) |

The exact sum before simplification already proves the result, independently of this optional closed-form table.

**5. Asymptotic fraction.** The six residue expressions show \(P(n)=11n^3/108+O(n^2)\), while \(E(n)=O(n^2)\) directly from its sum. Since \(\binom n3=n^3/6+O(n^2)\), the fraction tends to \((11/108)/(1/6)=11/18\). The earlier binary ghost-pulse theorem [1] constrains an unmodulated three-pulse support to a maximal arithmetic progression, of which there are only \(O(n^2)\), so the unmodulated fraction instead tends to zero.

## Verification

The standalone script `verify.py` enumerates every three-element support for all \(3\le n\le41\). For each support it directly enumerates all eight assignments of \(\pm1\) and all ordered triples of occupied indices, including repeated indices; this implementation does **not** assume the pair lemma. Independently it checks the three derived pair tests and the sum formula. All agree. The script additionally evaluates the closed-form cubic table and the floor-expression for \(2E(n)\) for every \(3\le n\le1000\), confirming the symbolic simplifications at those finite inputs. Sample counts appear in `weight3_counts.tsv`. Run using `python verify.py` with the Python standard library. The proof above, rather than the finite tests, establishes the infinite assertion.

## Relationship to prior work

Kashyap, Siegel, and Vardy introduced finite BGP/TGP constraints for optical channels [1]. Their Section III-A proves the arithmetic-progression classification and total count for **unmodulated** finite BGP words. Their Section IV-A lists the **total** number of TGP-feasible binary words for lengths through \(32\), without a weight-three layer formula, an all-length three-pulse classification, or the limiting three-pulse fraction. Their result for TGP with interaction range \(2\) applies to a different, weaker constraint. Their complementary Ramsey-theoretic treatment [2] classifies particular **bi-infinite** TGP supports, so its infinite extension requirements differ from the finite boundary condition used here. Neither inspected source gives the present finite-support layer enumeration or its \(11/18\) limit. Absence from these sources does not establish universal priority.

## Limitations

This is a theorem about the idealized finite ghost-pulse combinatorial condition and exactly three occupied slots. The result does **not** determine the capacity of the unrestricted TGP constraint, does not assert performance on a physical fiber-optic system, and does not extend automatically to four or more occupied slots. A previous unindexed equivalent formula remains possible. No external independent proof review has been performed.

## References

[1] N. Kashyap, P. H. Siegel, and A. Vardy, *Coding for the Optical Channel: The Ghost-Pulse Constraint*, arXiv:cs/0510033, first posted 2005-10-14; IEEE Transactions on Information Theory 52 (2006), 64–77; DOI: 10.1109/TIT.2005.860409. Accessible manuscript: https://ece.iisc.ac.in/~nkashyap/Papers/finite_gp.pdf.

[2] N. Kashyap, P. H. Siegel, and A. Vardy, *An Application of Ramsey Theory to Coding for the Optical Channel*, SIAM Journal on Discrete Mathematics 19 (2005), 921–937; DOI: 10.1137/S089548010444585X. Accessible text: https://cmrr-star.ucsd.edu/static/pubs/ramsey_coding_optical.pdf.
