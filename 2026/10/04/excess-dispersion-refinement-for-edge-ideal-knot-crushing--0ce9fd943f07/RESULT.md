# Excess-dispersion refinement for edge-ideal knot crushing

## Finding
Let \(K=K_1\#\cdots\#K_m\) be a composite knot with \(m\ge2\) nontrivial prime factors. Let \((\mathcal T,\ell)\) be an edge-ideal triangulation of \(K\), and write \(L=|\ell|\) for the number of ideal edges in its initial loop.

Consider a sequence of exactly \(m-1\) quad-vertex normal-sphere crushes in which every crush realizes a nontrivial connected-sum decomposition and the final components are edge-ideal triangulations of \(K_1,\ldots,K_m\). If the final ideal-loop lengths are \(d_1,\ldots,d_m\), then

\[
\sum_{i=1}^m d_i=L+2(m-1),
\qquad
\sum_{i=1}^m(d_i-1)=L+m-2.
\]

Let

\[
r=\left|\left\{i:d_i>1}\right\|.
\]

Then each of those \(r\) overlength prime components admits one additional prime-preserving crush, independently of the others. Hence

\[
|\mathcal T|\ge (m-1)+r+\sum_{i=1}^m \widetilde c(\mathbb S^3\setminus K_i).
\]

If \(H=\max_i(d_i-1)>0\), the exact excess identity gives

\[
r\ge \left\lceil\frac{L+m-2}{H}\right\rceil,
\]

so the preceding inequality has the corresponding explicit lower bound. In the important one-edge case \(L=1\), the total excess is exactly \(m-1\). Therefore, if every prime-output loop has length at most two, then \(r=m-1\) and

\[
|\mathcal T|\ge 2(m-1)+\sum_{i=1}^m \widetilde c(\mathbb S^3\setminus K_i).
\]

## Assumptions and scope
An edge-ideal triangulation is used in the sense of He--Sedgwick--Spreer: a triangulation of \(\mathbb S^3\) together with an embedded loop of edges representing the knot. The complexity \(\widetilde c(\mathbb S^3\setminus K_i)\) is the minimum tetrahedron count among edge-ideal triangulations of the prime knot \(K_i\).

The theorem is conditional on a chosen pure decomposition chain of \(m-1\) nontrivial connected-sum crushes ending at the prime factors. It does not assert that the dispersion parameter \(r\), or the concentration parameter \(H\), is determined by the knot alone. To turn the refined inequality into a stronger invariant lower bound than Proposition 26 of He--Sedgwick--Spreer, one must control \(r\) or \(H\) uniformly for complexity-minimizing starting triangulations.

## Proof
For a nontrivial decomposition crush, the crushed sphere meets the current ideal loop twice. He--Sedgwick--Spreer prove that when both resulting summands are nontrivial, every ideal segment survives as an ideal edge. Their Proposition 26 proof records the resulting bookkeeping explicitly: each such crush increases the total number of ideal edges by exactly two.

Starting with \(L\) ideal edges and applying exactly \(m-1\) such decomposition crushes therefore leaves a total of

\[
L+2(m-1)
\]

ideal edges distributed among the \(m\) prime-factor loops. This proves

\[
\sum_i d_i=L+2(m-1).
\]

Subtracting one baseline edge for each of the \(m\) prime components yields the exact excess identity

\[
\sum_i(d_i-1)=L+m-2.
\]

Now fix any prime-output component with \(d_i>1\). The proof of Lemma 25 in He--Sedgwick--Spreer applies to any nontrivial prime knot represented by an ideal loop of length greater than one: it constructs a suitable normal sphere and then a quad-vertex sphere whose crushing preserves the prime knot while strictly reducing the tetrahedron count. The \(r\) overlength prime outputs occupy distinct components, so one such prime-preserving crush can be carried out in each component without changing the other prime components.

Thus, after the original \(m-1\) decomposition crushes, at least \(r\) further crushes are available. Every crush strictly reduces the total number of tetrahedra by at least one. After these \(m-1+r\) crushes, the surviving knot components are still edge-ideal triangulations of the same prime factors, so their total number of tetrahedra is at least

\[
\sum_i \widetilde c(\mathbb S^3\setminus K_i).
\]

Rearranging gives

\[
|\mathcal T|\ge(m-1)+r+\sum_i\widetilde c(\mathbb S^3\setminus K_i).
\]

Finally, every positive excess \(d_i-1\) is at most \(H\), and the sum of these positive excesses is \(L+m-2\). Hence at least \(\lceil(L+m-2)/H\rceil\) indices are needed to carry the excess. This gives the stated concentration bound. If \(L=1\) and every \(d_i\le2\), each positive excess equals one and the exact total excess \(m-1\) forces \(r=m-1\).

## Verification
The proof was checked directly against the two source mechanisms on which it depends: the exact \(+2\) ideal-edge change for every nontrivial decomposition crush, and the prime-preserving crush available for every nontrivial prime loop of length greater than one. The first appears in the proof of Proposition 26; the second is the constructive content of the proof of Lemma 25.

Two boundary checks are useful. For \(m=2\) and \(L=1\), the excess is one, so necessarily \(r=1\), and the bound reduces to the published Proposition 26 bound; this matches the authors' observation that their proposed controlled-crushing improvement makes no difference for two summands. For \(m=3\), \(L=1\), a final length profile \((2,2,1)\) forces \(r=2\) and gives one more guaranteed crush than Proposition 26, whereas a profile \((3,1,1)\) has \(r=1\) and gives no improvement. This distinguishes dispersion of excess from its total amount.

No finite experiment is used as evidence for the infinite statement; the argument is symbolic and uses only the cited crushing lemmas plus integer bookkeeping.

## Relationship to prior work
He--Sedgwick--Spreer prove that every nontrivial connected-sum crush increases the ideal-edge count by two, observe a total excess of at least \(m-1\) after splitting into \(m\) prime factors, and use only the existence of one overlength prime component to obtain one additional crush and Proposition 26. They explicitly ask whether more controlled crushing can yield a stronger lower bound and ask whether Proposition 26 is ever tight.

The present lemma retains the full prime-output length profile instead of collapsing it to the statement that some component is overlength. It shows that every distinct overlength prime component contributes an independently guaranteed extra crush. Thus the relevant quantity for this route to stronger bounds is not only total excess but also its dispersion among prime factors. The published SoCG version states the same one-extra-crush argument and does not state the \(r\)-dependent refinement.

Targeted searches in the published published-finding corpus collection for edge-ideal excess, prime-output loop-length profiles, and controlled-crushing refinements returned no equivalent statement. The closest published-finding corpus items concern canonical torus-knot triangulation sizes and stick-number behavior under connected sum, not edge-ideal crushing profiles.

## Limitations
The theorem does not prove a universal improvement to Proposition 26 by itself. The parameter \(r\) depends on the chosen decomposition chain, and excess could concentrate in a single prime-output loop. Likewise, the \(H\)-bound is useful only when a nontrivial upper bound on concentration is available. No claim is made about tightness of Proposition 26 or about the exact edge-ideal complexity of any new composite knot.

Originality is supported by full inspection of the April 2025 arXiv version and the published SoCG 2025 version together with targeted published-finding corpus and web searches. A residual risk remains that an unindexed later note independently records the same bookkeeping refinement.

## References
1. Alexander He, Eric Sedgwick, Jonathan Spreer, *A Practical Algorithm for Knot Factorisation*, arXiv:2504.03942v1, first public 2025-04-04. See Lemma 22, Lemma 25, Proposition 26, and Question 28.
2. Alexander He, Eric Sedgwick, Jonathan Spreer, *A Practical Algorithm for Knot Factorisation*, 41st International Symposium on Computational Geometry (SoCG 2025), LIPIcs 332, Article 55, DOI:10.4230/LIPIcs.SoCG.2025.55.
