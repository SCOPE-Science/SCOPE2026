# Exact error-detecting open-location polynomials on the ternary projective-plane incidence graph

## Finding

Let \(G\) be the point-line incidence graph of the Desarguesian projective plane \(\operatorname{PG}(2,3)\). Write \(D_{\mathrm{DET}}(z)\) for the cardinality polynomial of its error-detecting open-locating-dominating (DET:OLD) vertex sets. Then

\[
D_{\mathrm{DET}}(z)=\bigl(234z^{10}+78z^{11}+13z^{12}+z^{13}\bigr)^2.
\]

Consequently, the minimum DET:OLD cardinality is \(20\), attained by exactly \(234^2=54{,}756\) different labeled vertex sets. They are **exactly** those whose omitted line vertices are three nonconcurrent lines and whose omitted point vertices are three noncollinear points; these choices are independent.

For comparison, if \(D_{\mathrm{RED}}(z)\) counts redundant open-locating-dominating sets, then

\[
D_{\mathrm{RED}}(z)=\bigl(234z^9+234z^{10}+78z^{11}+13z^{12}+z^{13}\bigr)^2,
\]

and the smallest RED:OLD sets have size \(18\). Thus two closely related one-fault models have distinct optimal detector counts on this natural regular incidence network. The previously known theory of double blocking sets already gives the RED:OLD minimum; it is not claimed as new here.

The expanded DET:OLD polynomial is

\[
54756z^{20}+36504z^{21}+12168z^{22}+2496z^{23}+325z^{24}+26z^{25}+z^{26}.
\]

## Assumptions and scope

The point and line classes of \(\operatorname{PG}(2,3)\) both have cardinality \(13\). Each point lies on \(4\) lines, and any two distinct points determine a unique line; dually, the same statements hold for lines. The incidence graph \(G\) is bipartite, with an edge between a point and a line precisely when they are incident.

For a detector set \(S\subseteq V(G)\), put \(N_S(v)=N_G(v)\cap S\). Following Jean and Seo, \(S\) is DET:OLD when every vertex satisfies \(|N_S(v)|\ge2\) and, for any distinct vertices \(u,v\), either

\[
|N_S(u)\setminus N_S(v)|\ge2
\quad\text{or}\quad
|N_S(v)\setminus N_S(u)|\ge2.
\]

It is RED:OLD when every vertex has at least two detectors in its open neighborhood and every pair satisfies \(|N_S(u)\triangle N_S(v)|\ge2\). These are conditions on **all** vertices, including detectors themselves. No assertion is made about other projective planes or other field orders.

## Proof

**1. Separation of the two bipartition sides.** Partition \(S=S_P\sqcup S_L\) into selected points and selected lines. For a point \(p\), \(N_S(p)\subseteq S_L\), whereas for a line \(\ell\), \(N_S(\ell)\subseteq S_P\). Under the common two-neighbor lower bound, any point and any line are automatically both \(2\)-distinguished and \(2^\#\)-distinguished. Thus the two parts can be analyzed independently and their cardinality-generating functions multiplied.

**2. The criterion for chosen lines.** Consider selected lines \(S_L\). Let \(d(p)\) be the number of selected lines through point \(p\). The two-neighbor condition says \(d(p)\ge2\) for every point. Two distinct points \(p,r\) have a unique common line. If that line is not selected, their selected-line neighborhoods are disjoint, each of cardinality at least two, and the DET pair condition holds. If their common line is selected, the two directional differences have sizes \(d(p)-1\) and \(d(r)-1\). They fail DET precisely when both degrees are two. Therefore:

\[
S_L\text{ is feasible on the point side}
\iff d(p)\ge2\text{ for all }p,
\text{ and every selected line contains at most one point with }d(p)=2.
\]

The dual criterion applies to selected points. For RED, the same geometry gives \(|N_{S_L}(p)\triangle N_{S_L}(r)|\ge2\) automatically as soon as both selected degrees are at least two. Hence RED feasibility on a side is exactly double covering.

**3. Omitted-line classification.** Write \(U\) for the omitted lines. Since four lines pass through each point, \(d(p)\ge2\) means at most two members of \(U\) concur at any point. In the dual plane, \(U\) is therefore a point set with no collinear triple (an arc). Such a set has at most four elements. Here is a short verification of this maximal-arc fact without a classification theorem: if an arc contained five points, its ten pair-secants would each contain two external points, making twenty incidences between secants and the eight external points. But any external point lies on at most two pair-secants (their endpoint pairs must be disjoint), giving at most sixteen incidences. This contradiction proves \(|U|\le4\).

If \(|U|=4\), its six pairwise intersection points are distinct and each has selected-line degree two. Each of those six weak points belongs to exactly two selected lines, producing twelve incidences between weak points and only nine selected lines. Some selected line contains at least two weak points, violating the DET criterion from Step 2. Conversely, if \(|U|=3\) and its lines are nonconcurrent, its three weak points are their pairwise intersections. The unique line joining any two of these weak points is one of the three omitted lines. Thus every selected line meets at most one weak point, and DET holds. For \(|U|\le2\), at most one weak point exists, so DET holds. A triple of concurrent omitted lines would violate the two-neighbor bound.

Therefore the permissible omitted-line sizes for DET are precisely \(0,1,2,3\), with the three-line sets nonconcurrent. Counts are respectively \(1\), \(13\), \(\binom{13}{2}=78\), and

\[
\binom{13}{3}-13\binom43=286-52=234.
\]

For RED, the admissible omitted-line sets are all arcs of sizes \(0\) through \(4\). An arc of size three is a triangle and has four extensions to four-point arcs, while every four-point arc has four triangle subsets. Thus four-point arcs also number \(234\).

**4. Combine the sides.** A chosen-line set has size \(13-|U|\). Its DET generating function is \(z^{13}+13z^{12}+78z^{11}+234z^{10}\); its RED generating function additionally has \(234z^9\). Projective duality gives identical factors for the chosen-point sets, and Step 1 makes the complete polynomials their respective squares. Their least powers, coefficients, and the stated classification of equality cases follow. \(\square\)

## Verification

The accompanying self-contained `verify.py` represents all points and lines as normalized nonzero vectors in \(\mathbb F_3^3\), with incidence determined by the vanishing dot product. It exhausts each of the \(2^{13}=8192\) possible choices on either side, reconstructing original open-neighborhood tests and separately using the weak-point criterion. All side masks agree in both models. It separately tests each of the \(54{,}756\) optimal full DET sets directly using the defining condition on all \(26\) graph vertices; another \(20{,}001\) deterministic mixed full-code choices are independently checked. The side count polynomials are multiplied and compared coefficient by coefficient with those stated. The order-two Fano plane is also checked as a control, but is not part of the theorem.

To reproduce with Python 3: `python3 verify.py`; successful completion prints `VERIFY_OK`. Exhaustive finite computation supports, but does not replace, the geometry proof above.

## Relationship to prior work

Jean and Seo (2023) define DET:OLD and RED:OLD using their two-neighbor and directed/symmetric distinction conditions, and examine complexity, extremal graphs, infinite grids, and cubic graphs. The theorem here applies their criteria to a different canonical family: the point-line incidence graph of \(\operatorname{PG}(2,3)\). Seo and Slater (2015) provide foundational fault-tolerant locating definitions.

Csajbók and Héger (2018 preprint; 2019 journal version) treat double blocking sets in finite projective planes. The RED criterion here is precisely double blocking independently on each side; the minimal RED cardinality is therefore within the established double-blocking framework. The additional directed pairwise requirement is what distinguishes DET and supplies the novel exact DET enumerator and extremizer classification.

## Limitations

The result is for one canonical finite incidence graph, not an asymptotic theorem or a classification for all plane orders. The originality comparison includes directly relevant accessible works but cannot rule out unpublished or differently named prior enumerations. No independent audit has been performed.

## References

- D. C. Jean and S. J. Seo, “On Error-detecting Open-locating-dominating sets,” arXiv:2306.12583v1 (first posted 21 June 2023), https://arxiv.org/html/2306.12583v1.
- B. Csajbók and T. Héger, “Double blocking sets of size \(3q-1\) in \(\operatorname{PG}(2,q)\),” arXiv:1805.01267 (first posted 3 May 2018), *European Journal of Combinatorics* 78 (2019), 73–89, https://doi.org/10.1016/j.ejc.2019.01.004.
- S. J. Seo and P. J. Slater, “Fault tolerant detectors for distinguishing sets in graphs,” *Discussiones Mathematicae Graph Theory* (2015), https://doi.org/10.7151/dmgt.1838.
