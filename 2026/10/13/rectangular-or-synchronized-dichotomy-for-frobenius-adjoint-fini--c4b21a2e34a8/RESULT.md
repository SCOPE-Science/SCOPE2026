# Rectangular-or-synchronized dichotomy for Frobenius-adjoint finite Gödel products

## Finding

**Theorem.** For every pair of integers \(m,n\geq2\), exactly
\[
N(m,n)=2^{m+n-4}+\binom{m+n-4}{m-2}
\]
ordered pairs of unary operations \((f,g)\) make the fixed product \(A=C_m\times C_n\) of finite Gödel chains into a Frobenius-adjoint residuated lattice with multiplication given by meet. More precisely, the common range \(D=f[A]=g[A]\) is either:

1. a **rectangle** \(I\times J\), where \(I\subseteq C_m\) and \(J\subseteq C_n\) each contain their bottom and top elements; or
2. a **synchronized diagonal** \(\{(a_0,b_0),\ldots,(a_r,b_r)\}\), with \(a_0=b_0=0\), \(a_r=m-1\), \(b_r=n-1\), and \(a_i<a_{i+1}\), \(b_i<b_{i+1}\) for every \(i<r\).

The two types are disjoint when \(m,n\geq2\). Conversely, each listed set is the common range of precisely one valid pair. The count is for operations on the given coordinate-labelled algebra; it is not a count up to algebra isomorphism. The first nontrivial examples are \(N(2,2)=2\), \(N(3,3)=6\), and \(N(4,4)=22\).

## Assumptions and scope

Write \(C_m=\{0,1,\ldots,m-1\}\), ordered naturally, with bottom \(0\) and top \(m-1\). On \(A=C_m\times C_n\), all inequalities and lattice operations are coordinatewise; the monoidal product is meet, and the residuum is the coordinatewise Gödel implication
\[
i\Rightarrow j=\begin{cases}\mathrm{top},&i\leq j,\\j,&i>j.\end{cases}
\]
The identities defining the counted expansions, for all \(x,y\in A\), are
\[
\begin{aligned}
&f(x)\leq x,\\
&g(x)\leq y\quad\Longleftrightarrow\quad x\leq f(y),\\
&f(g(x)\to y)=g(x)\to f(y),\\
&f(g(x)\vee y)=g(x)\vee f(y),\\
&g(x\wedge g(y))=g(x)\wedge g(y).
\end{aligned}
\]
These are the interiority, adjunction and Frobenius conditions from the Frobenius-adjoint residuated lattice definition in Wang--Shi--Wang (2026), specialized to finite Gödel algebras. The result makes no claim about products of three or more chains, arbitrary residuated multiplication, or isomorphism classes.

## Proof

**Step 1: a common subalgebra core.** An adjunction makes \(g\) order-preserving and join-preserving, in particular \(g(0)=0\), and yields the unit \(x\leq f(g(x))\) and counit \(g(f(y))\leq y\). Since \(f\leq\mathrm{id}\), the unit implies \(x\leq g(x)\), so \(g(1)=1\). The last Frobenius law with \(x=1\) then gives \(g(g(y))=g(1)\wedge g(y)=g(y)\): \(g\) is an extensive, idempotent closure operator.

In the join Frobenius law put \(y=0\). Since \(f(0)=0\), we obtain \(f(g(x))=g(x)\). Conversely, if \(f(c)=c\), the counit gives \(g(c)\leq c\), hence \(g(c)=c\). Thus the fixed points of both maps agree. To see that every value \(f(y)\) is fixed, note that \(g(g(f(y)))=g(f(y))\leq y\); the adjunction then gives \(g(f(y))\leq f(y)\), and extensivity forces equality. Therefore the common fixed-point set is also the common range \(D=f[A]=g[A]\).

The maps must be the respective floor and ceiling onto \(D\): for any \(d\in D\), adjunction and \(g(d)=d\) give \(d\leq f(y)\) if and only if \(d\leq y\), so \(f(y)\) is the greatest element of \(D\) below \(y\); and closure gives \(g(x)\) as the least element of \(D\) above \(x\). The set \(D\) contains \(0,1\) and is closed under \(\wedge,\vee,\to\). Indeed, a right adjoint preserves meets, a left adjoint preserves joins, the final Frobenius identity forces the meet of fixed points to be fixed, and the implication Frobenius law with fixed \(c,d\) gives \(f(c\to d)=c\to f(d)=c\to d\).

**Step 2: a nonzero axis point forces a rectangle.** Suppose \((a,0)\in D\) with \(a>0\). Its implication into the bottom is \((a,0)\to(0,0)=(0,n-1)\); closure of \(D\) under implication places that top vertical-axis point in \(D\). Taking its implication into the bottom similarly puts \((m-1,0)\in D\). For any \((u,v)\in D\), meet with these two points yields \((u,0),(0,v)\in D\). By joins, every pair of coordinates from the two projections of \(D\) also belongs to \(D\), so \(D=I\times J\). The projections are endpoint-containing subchains. The same argument starts from any nonzero point on the other axis.

**Step 3: absence of axis points forces synchronized strict increase.** Now suppose \(D\) has no nonzero horizontal- or vertical-axis point. Set \(e=(m-1,0)\) and \(h=(0,n-1)\). The floor description gives \(f(e)=f(h)=0\). The join Frobenius law with \(x=e,y=h\) says
\[
f(g(e)\vee h)=g(e)\vee f(h)=g(e).
\]
As \(g(e)\geq e\), the argument on the left is \(1\). Thus \(g(e)=f(1)=1\). Symmetrically \(g(h)=1\). For any fixed \(d=(u,v)\in D\), the meet Frobenius law now gives
\[
g((u,0))=g(e\wedge d)=g(e)\wedge d=d,
\quad
g((0,v))=g(h\wedge d)=g(h)\wedge d=d.
\]
Hence distinct fixed points can share neither their first nor their second coordinate. Also, if \(u<u'\), monotonicity of \(g\) forces \(g((u,0))\leq g((u',0))\); thus their second coordinates are strictly increasing as well. Since \(0,1\in D\), this is exactly the stated synchronized diagonal type.

**Step 4: both types realize the axioms.** For any listed \(D\), define \(g(x)\) to be its least element above \(x\) and \(f(y)\) its greatest element below \(y\). Both extrema exist. The adjunction and interiority are immediate. For a rectangular \(D=I\times J\), these maps act coordinatewise as ceiling and floor onto endpoint-containing subchains. In one finite chain, a case split at \(y\geq c\), for each fixed \(c\), proves \(f(c\to y)=c\to f(y)\) and \(f(c\vee y)=c\vee f(y)\); splitting at \(x\geq c\) proves \(g(x\wedge c)=g(x)\wedge c\). Products inherit all identities coordinatewise.

For a synchronized diagonal \(D\), its elements form a chain whose successive points rise *strictly in both coordinates*. Fix \(c\in D\), and let \(d=g(x)\). If \(d\leq c\), then \(x\leq c\), so \(g(x\wedge c)=d=d\wedge c\). If \(d>c\), then \(x\not\leq c\); some coordinate of \(x\wedge c\) equals the corresponding coordinate of \(c\), precluding any strictly smaller diagonal point from dominating \(x\wedge c\), while \(c\) itself dominates it. This proves the meet Frobenius law. For the join law let \(d=f(y)\). If \(d\geq c\), then \(y\geq c\) and both sides equal \(d\). If \(d<c\), then \(c\leq c\vee y\), but no diagonal point strictly above \(c\) can lie below \(c\vee y\), since that would also lie below \(y\), contradicting \(d<c\). Thus \(f(c\vee y)=c=c\vee d\).

Finally, if \(d=f(y)\geq c\), then \(y\geq c\), so both sides of \(f(c\to y)=c\to f(y)\) are \(1\). Otherwise \(d<c\) and \(y\not\geq c\). At least one coordinate of \(y\) lies strictly below the corresponding coordinate of \(c\). In the Gödel implication \(c\to y\), such deficient coordinates are unchanged, while any remaining coordinate is replaced by the top. No fixed point at or above \(c\) can lie below \(c\to y\). Among fixed points below \(c\), the condition of lying below \(c\to y\) is equivalent to lying below \(y\), because every nondeficient coordinate of \(y\) already exceeds that of \(c\). Hence \(f(c\to y)=f(y)=d=c\to d\), using strict increase in both coordinates. All five identities hold.

**Step 5: count.** Rectangles correspond bijectively to independent choices of the \(m-2\) and \(n-2\) interior chain points, giving \(2^{m+n-4}\) choices. A synchronized diagonal with exactly \(k\) interior points corresponds bijectively to a \(k\)-element subset of the \(m-2\) interior first coordinates and a \(k\)-element subset of the \(n-2\) interior second coordinates, matched in increasing order. Thus there are
\[
\sum_{k=0}^{\min(m-2,n-2)}\binom{m-2}{k}\binom{n-2}{k}
=\binom{m+n-4}{m-2}
\]
diagonals, by Vandermonde's identity. The types are disjoint, and each core determines exactly one adjoint pair; summing proves the formula.

## Verification

Run `python3 farl_twochain_verify.py` with Python's standard library. The program (a) enumerates all endpoint-containing meet/join/implication subalgebras and checks every defining axiom against their floor/ceiling maps for the six chain-size pairs \((2,2),(2,3),(3,3),(3,4),(4,4),(3,5)\); and independently (b) enumerates all join-preserving maps from the generators on coordinate axes, computes their right adjoints, and checks the axioms for \((2,2),(2,3),(3,3),(3,4)\). Both approaches reproduce the two-type counts, with no other types, and print `VERIFY_OK`. The raw-adjoint enumeration checks 16, 108, 1,296, and 12,000 candidate maps respectively. These checks are finite corroboration; the proof establishes the formula for all \(m,n\geq2\).

## Relationship to prior work

Wang, Shi and Wang (2026, Definition 3.8) introduce the Frobenius-adjoint residuated algebraic language and study algebraization and categorical semantics. Castaño, Cimadamore, Díaz Varela and Rueda (2020, Lemma 1.1 and the following discussion) had already characterized common quantifier ranges as suitably relatively complete Gödel subalgebras and represented quantifiers by floors and ceilings. **The common-core idea and the general relative-completeness framework are not claimed as new.** The present result instead identifies, for the fixed *two-chain product*, exactly which cores occur and gives the resulting closed count; no equivalent two-factor dichotomy or count was located in the inspected primary texts or the queried published mathematical records. This negative search is not a proof of global novelty.

## Limitations

The count distinguishes operations on a fixed product, rather than classes under factor interchange or other automorphisms. It covers only meet-multiplication Gödel residuated products of exactly two nontrivial finite chains. The original 2020 relative-completeness theory is a known general framework; an unlocated earlier specialization of that framework to two finite chains remains an originality risk. Finite verification is not an infinite proof, and this research has not undergone independent audit.

## References

- Juntao Wang, Jieqiong Shi and Mei Wang, *Frobenius Galois expansions of substructural logics: Algebraization, Kalman equivalence and positive cone semantics*, arXiv:2609.09529v1 (first posted September 8, 2026), especially Definition 3.8. https://arxiv.org/abs/2609.09529
- Diego Castaño, Cecilia Cimadamore, José Patricio Díaz Varela and Laura Rueda, *An algebraic study of S5-modal Gödel logic*, arXiv:2006.10180v1 (first posted June 17, 2020), especially Lemma 1.1 and the discussion of \(m\)-relatively complete subalgebras. https://arxiv.org/html/2006.10180v1
