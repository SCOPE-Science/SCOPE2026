# Secure-total-domination polynomial of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). For a vertex set \(S\), put
\[
I=\{i:a_i\in S\},\qquad J=\{i:b_i\in S\}.
\]
Then \(S\) is a secure total dominating set exactly when
\[
|I|\ge2,\qquad |J|\ge2,
\]
and both conditional inequalities
\[
I=[n]\ \text{or}\ |J|\ge3,
\qquad
J=[n]\ \text{or}\ |I|\ge3
\]
hold. Therefore the polynomial that counts every secure total dominating set by cardinality is
\[
\operatorname{ST}_n(x)
=
\left(\sum_{k=3}^{n}\binom{n}{k}x^k\right)^2
+2\binom{n}{2}x^{n+2}.
\]
In particular,
\[
\gamma_{st}(\operatorname{Cr}_3)=5,
\]
with six minimum sets, while
\[
\gamma_{st}(\operatorname{Cr}_n)=6\qquad(n\ge4).
\]
The number of minimum secure total dominating sets is \(28\) when \(n=4\), and \(\binom{n}{3}^2\) when \(n\ge5\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A total dominating set \(S\) has the property that every vertex has a neighbor in \(S\). A total dominating set is secure total dominating when, for every \(u\notin S\), some adjacent defender \(v\in S\) can be replaced by \(u\) so that \((S\setminus\{v\})\cup\{u\}\) is again total dominating. The result is for every integer \(n\ge3\), and counts all such sets rather than only minimum ones.

The archive date attached to this result is the earliest exact calendar day verified among the inspected public sources that state the standard secure-total-domination notion. The original introduction by Benecke, Cockayne, and Mynhardt is bibliographically recorded as November 2007, but the inspected metadata does not provide an exact day, so no day was invented for that earlier source.

## Proof
First characterize total domination. Every vertex \(a_i\) must have a selected neighbor in \(B\). Since \(a_i\) is adjacent to every \(b_j\) except \(b_i\), this holds for all \(i\) exactly when \(|J|\ge2\): zero selected \(B\)-vertices plainly fails, while if \(J=\{i\}\), the vertex \(a_i\) has no selected neighbor. Two or more selected \(B\)-vertices suffice because at most one can have index \(i\). By symmetry, all vertices of \(B\) are totally dominated exactly when \(|I|\ge2\). Hence
\[
S\text{ is total dominating}\quad\Longleftrightarrow\quad |I|\ge2\text{ and }|J|\ge2.
\]

Now let \(a_k\notin S\). Any defender of \(a_k\) lies in \(B\), say \(b_j\in S\) with \(j\ne k\). After the swap, the selected index sets are
\[
I'=I\cup\{k\},\qquad J'=J\setminus\{j\}.
\]
The preceding total-domination criterion says the swapped set is total dominating exactly when \(|I'|\ge2\) and \(|J'|\ge2\). The first inequality is automatic because the original set already has \(|I|\ge2\), while the second is equivalent to \(|J|\ge3\). Conversely, if \(|J|\ge3\), then for every outside \(a_k\) there is a choice of \(j\in J\setminus\{k\}\); deleting that defender leaves at least two selected \(B\)-vertices, so the swap is valid. Therefore the security condition for all outside vertices of \(A\) is exactly
\[
I=[n]\quad\text{or}\quad |J|\ge3.
\]
The symmetric argument gives
\[
J=[n]\quad\text{or}\quad |I|\ge3.
\]
Together with total domination, these four conditions prove the classification.

To count sets, all pairs \((I,J)\) with \(|I|,|J|\ge3\) contribute
\[
\left(\sum_{k=3}^{n}\binom{n}{k}x^k\right)^2.
\]
The only remaining possibilities are \(|I|=2\) with \(J=[n]\), or \(|J|=2\) with \(I=[n]\). Each family has \(\binom{n}{2}\) members of size \(n+2\), yielding the stated extra term.

The minimum terms follow directly. For \(n=3\), only the exceptional term has degree five, with coefficient \(2\binom32=6\). For \(n=4\), degree six receives \(\binom43^2=16\) sets from the square plus \(2\binom42=12\) exceptional sets, totaling \(28\). For \(n\ge5\), the exceptional term has degree at least seven, so the degree-six coefficient is \(\binom n3^2\).

## Verification
The standalone verifier exhaustively constructs \(\operatorname{Cr}_n\), tests every vertex subset against the definition of secure total domination, and compares the resulting size distribution with the closed polynomial for \(3\le n\le8\). It independently checks the four-condition classification for every subset in the same range and checks the stated minimum values and multiplicities. The verification is finite evidence supporting the proof, not a substitute for the all-\(n\) argument.

## Relationship to prior work
Benecke, Cockayne, and Mynhardt introduced secure total domination in 2007. Klostermeyer and Mynhardt subsequently studied secure domination and secure total domination together; the inspected full-text material states the standard definition and includes a complete-bipartite example, but no crown-graph, perfect-matching-deletion, or equivalent all-set polynomial statement was found. Duginov later established bounds and computational-complexity results for secure total domination, including hard bipartite classes.

A published result on complete multipartite graphs gives a secure-total-domination polynomial for that class. It does not subsume the present theorem: \(\operatorname{Cr}_n\) is obtained from \(K_{n,n}\) by deleting a perfect matching and is not a complete multipartite graph for \(n\ge3\). The difference is substantive even at the scalar level: the complete bipartite graph \(K_{n,n}\) has secure total domination number four in the inspected literature, whereas the crown graph has value six for every \(n\ge4\). The present result determines the entire secure-total-dominating-set distribution after that structured edge deletion.

## Limitations
The originality assessment is literature-based rather than a proof of global novelty. Searches covered the aliases “crown graph,” “complete bipartite graph minus a perfect matching,” “complete bipartite graph minus a 1-factor,” and “bipartite Kneser graph \(H(n,1)\),” together with secure-total-domination terminology. A poorly indexed or inaccessible source could still contain an equivalent result. The original 2007 introduction was located only with month-level publication metadata, so the recorded exact date comes from the earliest inspected source for which an exact public day was verifiable; this does not assert that the concept originated on that later day.

## References
1. S. Benecke, E. J. Cockayne, C. M. Mynhardt, “Secure total domination in graphs,” Utilitas Mathematica 74 (2007), 247–259.
2. W. F. Klostermeyer, C. M. Mynhardt, “Secure domination and secure total domination in graphs,” Discussiones Mathematicae Graph Theory 28(2), 267–284, DOI 10.7151/dmgt.1405.
3. O. Duginov, “Secure total domination in graphs: bounds and complexity,” Discrete Applied Mathematics 222, 97–108, DOI 10.1016/j.dam.2016.08.018.
