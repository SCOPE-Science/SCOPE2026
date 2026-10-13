# Strong-resolving polynomials of finite projective-plane incidence graphs

## Finding

Let \(\Pi\) be **any** finite projective plane of order \(q\geq2\), including a non-Desarguesian plane when one exists, and put \(n=q^2+q+1\). Write \(G_\Pi\) for its bipartite point–line incidence graph, with \(n\) points and \(n\) lines. The **strong-resolving polynomial** is
\[
R_\Pi(z)=\sum_{\substack{S\subseteq V(G_\Pi)\\ S\text{ strongly resolves }G_\Pi}}z^{|S|}.
\]
It is independent of the isomorphism type of \(\Pi\) and equals
\[
\boxed{R_\Pi(z)=z^{2n}\left[2(1+z^{-1})^n-1+2nz^{-1}\big((1+z^{-1})^{q+1}-1\big)-n(q+1)z^{-2}\right].}
\]
This is a polynomial: the displayed Laurent expression has only nonnegative powers after multiplication. Equivalently, the polynomial counting complements of strong-resolving sets by their size is
\[
\boxed{I_\Pi(t)=2(1+t)^n-1+2nt\big((1+t)^{q+1}-1\big)-n(q+1)t^2.}
\]
In particular, the **strong metric dimension** is \(\operatorname{sdim}(G_\Pi)=n\), and the only two minimum strong-resolving sets are the set of all points and the set of all lines.

The inclusion-minimal strong-resolving sets (where removing any selected vertex destroys strong resolution) have exactly two possible sizes. Two have size \(n\), and exactly \(2n\) have size \(2n-q-2=2q^2+q\). The latter are complements of a point together with every line through it, or dually of a line together with every point on it. Thus the gap between the sizes of inclusion-minimal and minimum strong-resolving sets is \(q^2-1\).

## Assumptions and scope

A finite projective plane of order \(q\) has \(n=q^2+q+1\) points and lines, with \(q+1\) incidences at each point or line, exactly one line through any two distinct points, and exactly one intersection point for any two distinct lines. No coordinatization or field is assumed.

For distinct vertices \(u,v\) of a connected graph, a vertex \(w\) **strongly resolves** them when a shortest \(u\)-to-\(w\) path contains \(v\), or a shortest \(v\)-to-\(w\) path contains \(u\). Equivalently, \(d(w,u)=d(w,v)+d(u,v)\) or \(d(w,v)=d(w,u)+d(u,v)\). A set strongly resolves the graph if this holds for every unordered pair of distinct vertices. An unordered pair \(\{u,v\}\) is **mutually maximally distant** (MMD) if all neighbors of each endpoint are no farther from the other endpoint than their mutual distance.

All assertions quantify over every \(q\geq2\) for which a projective plane exists and every choice of such a plane. They are not assertions about the ordinary (weak) metric dimension or about an arbitrary bipartite graph.

## Proof

**Step 1: A general reduction.** In any finite connected graph, a set \(S\) strongly resolves the graph if and only if it contains at least one endpoint of every MMD pair. To see necessity, suppose \(u,v\) are MMD and a vertex \(w\notin\{u,v\}\) strongly resolves them. If, for example, \(d(w,u)=d(w,v)+d(u,v)\), the first neighbor \(x\) of \(v\) on a shortest \(v\)-to-\(w\) path has \(d(u,x)=d(u,v)+1\), contradicting maximality of \(v\) relative to \(u\). The other ordering is symmetric. For sufficiency, take a shortest path between any two vertices \(a,b\). Extend it at either end whenever it remains a shortest path between its enlarged endpoints. Finiteness ensures termination. The two endpoints \(u,v\) of the resulting geodesic are MMD, for otherwise an extending neighbor would exist. By assumption one of \(u,v\) belongs to \(S\), and as an endpoint of a geodesic containing \(a,b\) this selected vertex strongly resolves \(a,b\). Thus \(S\) is a vertex cover of the graph of MMD pairs precisely when it strongly resolves \(G\).

**Step 2: MMD pairs for a projective plane.** In \(G_\Pi\), distinct points have distance two, distinct lines have distance two, an incident point–line pair has distance one, and a nonincident point–line pair has distance three. Thus nonincident point–line pairs are MMD because three is the diameter. A pair of distinct points is not MMD: there exists a line through the first but not the second (since \(q+1\geq3\)); it is a neighbor of the first at distance three from the second, exceeding the two between the points. The argument for two lines is dual. An incident point–line pair is not MMD, since a different line through the point is a neighbor at distance two from the original line, exceeding one. Hence the MMD graph is **exactly the point–line nonincidence graph**, whose edges are pairs \((p,\ell)\) with \(p\notin\ell\).

**Step 3: Characterization.** By Steps 1–2, \(S\) strongly resolves \(G_\Pi\) precisely when its complement \(T\) has no nonincidence edge. Write \(T=A\cup B\), where \(A\) is a set of points and \(B\) a set of lines. The condition is
\[
\boxed{\text{Every point of }A\text{ lies on every line of }B.}
\]
When one of \(A,B\) is empty, the other can be chosen arbitrarily. When both are nonempty, it is impossible for each to have size at least two: any two distinct points have only one common line. Consequently every mixed admissible pair \((A,B)\) has either \(|A|=1\) and \(1\leq|B|\leq q+1\), or \(|B|=1\) and \(1\leq|A|\leq q+1\).

**Step 4: Count all sets.** The two pure cases contribute \(2(1+t)^n-1\) to the complement polynomial, where the empty set is counted just once. For one specified point, there are \(\binom{q+1}{j}\) choices of \(j\geq1\) concurrent incident lines. Summing over the \(n\) points contributes \(nt((1+t)^{q+1}-1)\); the dual case contributes the same. Each single incident point–line pair was counted twice in these mixed families, so subtract \(n(q+1)t^2\). This proves the asserted expression for \(I_\Pi\), and complementation gives \(R_\Pi(z)=z^{2n}I_\Pi(z^{-1})\).

**Step 5: Bases and inclusion-minimal sets.** The largest admissible pure complement has size \(n\); a mixed admissible complement has size at most \(q+2<n\), because \(n-(q+2)=q^2-1>0\). Therefore the maximum independent sets of the MMD graph are exactly the complete point part and the complete line part; their complements are the two strong metric bases, each of size \(n\).

An admissible complement is inclusion-maximal either if it is one complete pure part or if it is mixed and consists of a single point and *all* \(q+1\) lines incident with it, or dually a single line and *all* \(q+1\) points incident with it. Indeed, a mixed set with at least two lines has only its common intersection point available on the point side and can be enlarged on the line side until all lines through that point are present; the remaining configurations follow by duality. These \(2n+2\) maximal complements are distinct. Their complements give precisely all inclusion-minimal strong-resolving sets and their asserted sizes and multiplicities. This completes the proof.

## Verification

The standalone, dependency-free `verify.py` constructs the incidence graphs of \(\mathrm{PG}(2,2)\) and \(\mathrm{PG}(2,3)\) directly from normalized nonzero coordinate vectors and the dot-product incidence relation. It computes all pairwise distances, tests the graph of MMD pairs against the projective nonincidence condition, exhaustively counts admissible complements and maximal ones, and compares the enumerators with the displayed polynomial. For \(q=2\), it independently checks every one of the \(2^{14}=16384\) vertex subsets against the defining distance-equality strong-resolution test for every vertex pair.

Run `python3 verify.py`; successful output includes `VERIFY_OK PG(2,2) ... all_independent_sets=332 strong_bases=2`, `VERIFY_OK PG(2,3) ... all_independent_sets=16721 strong_bases=2`, and `VERIFY_FINISHED all invariants established`. The finite computations check the instances \(q=2,3\); the preceding argument, not an extrapolation from those checks, proves the theorem for all projective planes.

## Relationship to prior work

Oellermann and Peters-Fransen introduced strong metric dimension and its connection to MMD vertex covers; this general reduction is standard and explicitly credited. A full-text survey of strong metric dimension confirms this reduction and was checked for projective-plane specializations. Héger and Takáts investigated **ordinary** resolving and semi-resolving sets of finite projective-plane incidence graphs. Ordinary distance-vector resolution is not equivalent to strong geodesic resolution, so their bounds and constructions do not enumerate the sets treated here.

A published projective point–hyperplane **nonincidence** graph theorem concerns total dominating sequences and total-uniformity. It uses the same auxiliary graph family but does not establish its independent-set polynomial, its maximal independent sets, or the strong-resolving structure of the incidence graph. No cited source implies the complete all-size polynomial or the two-size inclusion-minimal classification. Literature searches are not a proof of priority; see limitations.

## Limitations

The theorem applies to projective planes (not arbitrary linear spaces), and requires \(q\geq2\). It concerns strong metric resolution, not ordinary metric dimension. Enumeration of all nonisomorphic projective planes is neither needed nor claimed. The verifier checks only the prime-field planes of orders two and three, whereas the proof covers even non-Desarguesian planes. The 2007 foundational paper's complete publisher text was not accessible through the checked legal sources; its general reduction was corroborated by a separately inspected survey and independently reconstructed in Step 1. An earlier unindexed or differently phrased enumeration could affect research priority, but not the proof.

## References

1. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, Discrete Applied Mathematics **155** (2007), 356–364; DOI: 10.1016/j.dam.2006.06.009 (foundational reduction).
2. J. Kratica, V. Kovačević-Vujčić, M. Čangalović, and N. Mladenović, *Strong metric dimension: A survey*, Yugoslav Journal of Operations Research **24** (2014), survey PDF: https://yujor.fon.bg.ac.rs/index.php/yujor/article/download/390/383/370 (full text inspected, strong resolving graph theorem).
3. T. Héger and A. Takáts, *Resolving Sets and Semi-Resolving Sets in Finite Projective Planes*, Electronic Journal of Combinatorics **19**(4) (2012), P30, public 2012-11-22, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v19i4p30/pdf/ (ordinary metric resolution; full text inspected).
4. *Projective nonincidence graphs realize every even total-uniformity*, published research result, https://github.com/published-finding corpus/2026/blob/main/2026/9/21/SCOPE-projective-nonincidence-total-even-uniformity--90b1f31fb0b4/RESULT.md (same auxiliary family, distinct invariant; full RESULT inspected).
