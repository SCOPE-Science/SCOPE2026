# Three-piece rotated odometers: universal aperiodicity and three exact return laws

## Finding

For **each** permutation \(\pi\in S_3\), let \(F_\pi=\mathfrak a\circ R_\pi\) be the rotated von Neumann–Kakutani map on \(I=[0,1)\), where \(R_\pi\) rearranges three successive intervals of equal length. Each of these six maps is **aperiodic at every point** and has **Lebesgue measure as its unique invariant Borel probability**. Moreover, for \(L=[0,1/4)\), its first-return map is a rescaled rotated odometer \(F_{\pi_1}\), with an exactly classified triple of first-return times \((h_0,h_1,h_2)\) on the three equal pieces of \(L\):

| One-line permutation \(\pi\) | Induced permutation \(\pi_1\) | Return-time triple \((h_0,h_1,h_2)\) | Conditional return-time variance |
|:--|:--|:--|--:|
| (0,1,2) | (0,1,2) | (4,4,4) | 0 |
| (0,2,1) | (1,2,0) | (2,2,8) | 8 |
| (1,0,2) | (1,2,0) | (2,2,8) | 8 |
| (1,2,0) | (1,2,0) | (4,4,4) | 0 |
| (2,0,1) | (2,0,1) | (10,1,1) | 18 |
| (2,1,0) | (2,0,1) | (10,1,1) | 18 |

Here one-line notation means \(\pi=(\pi(0),\pi(1),\pi(2))\). The return-time distribution assigns probability \(1/3\) to each entry of the triple when the initial point is uniformly sampled from \(L\), and its mean is always exactly \(4\). Repeated entries contribute their respective multiplicities.

## Assumptions and scope

For every integer \(n\geq1\) and every \(x\in[1-2^{1-n},1-2^{-n})\), define

\[
\mathfrak a(x)=x-1+3\cdot2^{-n}.
\]

For each \(i\in\{0,1,2\}\) and \(x\in[i/3,(i+1)/3)\), define

\[
R_\pi(x)=x+\frac{\pi(i)-i}{3},\qquad F_\pi=\mathfrak a\circ R_\pi.
\]

All intervals are half-open as written: the endpoint \(0\) is in \(I\), the endpoint \(1\) is not, and there are no unspecified tie-breaking or almost-everywhere conventions. The first return time \(\tau_\pi(x)\) is the smallest positive integer \(t\) with \(F_\pi^t(x)\in L\). For \(i\in\{0,1,2\}\) put \(J_i=[i/12,(i+1)/12)\subset L\). The entries \(h_i\) in the table satisfy \(\tau_\pi(x)=h_i\) **for every** \(x\in J_i\). The assertion about invariant probabilities concerns ordinary Borel probabilities on \(I\), not topological unique ergodicity on the noncompact half-open interval under a compactification.

## Proof

**Step 1: an exhaustive 12-cell return graph.** Partition \(I\) into \(J_j=[j/12,(j+1)/12)\), now indexed by \(0\leq j\leq11\). Set

\[
k_\pi(j)=4\pi(\lfloor j/4\rfloor)+(j\bmod4).
\]

The finite rearrangement maps \(J_j\) onto \(J_{k_\pi(j)}\). The adding map satisfies

\[
\mathfrak a(J_k)=J_{k+6}\ \ (0\leq k\leq5),\qquad
\mathfrak a(J_k)=J_{k-3}\ \ (6\leq k\leq8).
\]

For \(9\leq k\leq11\), \(\mathfrak a(J_k)\subset L\); more precisely, on the entire high quarter,

\[
\mathfrak a(3/4+w)=\tfrac14\mathfrak a(4w),\qquad 0\leq w<1/4.
\]

Thus a 12-cell itinerary follows \(j\mapsto k_\pi(j)+6\) for \(k_\pi(j)<6\), or \(j\mapsto k_\pi(j)-3\) for \(6\leq k_\pi(j)\leq8\), terminating when \(k_\pi(j)\geq9\). Starting separately from \(j=0,1,2\), direct finite evaluation gives the *complete* itineraries below; the final digit in each itinerary is the last cell **before** re-entry to \(L\).

| \(\pi\) | Itinerary from \(J_0\) | From \(J_1\) | From \(J_2\) |
|:--|:--|:--|:--|
| (0,1,2) | 0–6–3–9 | 1–7–4–10 | 2–8–5–11 |
| (0,2,1) | 0–6 | 1–7 | 2–8–10–3–9–11–4–5 |
| (1,0,2) | 0–10 | 1–11 | 2–3–4–6–8–5–7–9 |
| (1,2,0) | 0–10–8–6 | 1–11–9–7 | 2–3–4–5 |
| (2,0,1) | 0–5–7–9–11–4–6–8–10–3 | 1 | 2 |
| (2,1,0) | 0–5–11–9–7–4–10–8–6–3 | 1 | 2 |

In **each row**, the three itineraries are pairwise disjoint and together contain every integer from \(0\) through \(11\) exactly once. This is an exhaustive finite identity, not a sample of numerically iterated trajectories. It proves the return-time triples by counting their cell lengths; it also proves that the corresponding finite Kakutani towers partition all of \(I\), so *every point of \(I\) eventually enters \(L\)*.

At the last cell of the itinerary starting in \(J_i\), the rearrangement sends it to \(J_{9+\pi_1(i)}\), with \(\pi_1\) as listed above. Since all preceding moves were translations by integer multiples of \(1/12\), the return map \(G_\pi:L\to L\) satisfies, pointwise on each \(J_i\),

\[
G_\pi(x)=\tfrac14\mathfrak a\!\left(4x+\frac{\pi_1(i)-i}{3}\right)
=\tfrac14 F_{\pi_1}(4x).
\]

This establishes the claimed induced-map conjugacy including all half-open endpoints.

**Step 2: no periodic points, for any permutation.** Three permutations are fixed by induction: \((0,1,2)\), \((1,2,0)\), and \((2,0,1)\). Take any one of these. Suppose it has a periodic orbit \(\mathcal P\). Every orbit enters \(L\), so \(\mathcal P\cap L\ne\varnothing\). On \(L\) the first-return map is the same rotated odometer, rescaled by \(x\mapsto4x\), and every orbit of this induced map enters its own first quarter. Inductively \(\mathcal P\) has a point in \([0,4^{-m})\) for every positive integer \(m\). Since \(\mathcal P\) is finite, this forces \(0\in\mathcal P\). But \(\mathfrak a(I)=(0,1)\), and thus \(F_\pi(I)\subset(0,1)\); in particular, no periodic orbit can contain \(0\). Contradiction. For any of the other three permutations, every orbit enters \(L\), and the first return is a rescaled map of cyclic type \((1,2,0)\) or \((2,0,1)\). A periodic orbit for the original would induce a periodic orbit for that cyclic type, again impossible.

**Step 3: the invariant probability is unique.** Each \(F_\pi\) preserves Lebesgue measure, since it is a composition of interval exchanges (up to the single missing image point). The identity permutation gives the classical uniquely ergodic dyadic adding machine. For the two cyclic permutations, Bruin–Lukina, *Rotated Odometers*, Proposition 8.4, proves that the aperiodic compactification is conjugate to the dyadic odometer by stationary primitive diagram methods. Step 2 removes all periodic components. Every invariant probability on \(I\) is atomless: a positive atom would have a positive mass at infinitely many distinct forward iterates, contradicting finite total mass (the map is injective on \(I\)). Hence its countable discontinuity-boundary lifts contribute no mass, and the cited compactification result implies a unique invariant probability, namely Lebesgue measure, for each cyclic type.

For a transposition \(\pi\), let \(\mu\) be any invariant Borel probability. Because the towers in Step 1 partition \(I\), \(\mu(L)>0\). The normalized restriction \(\nu=\mu|_L/\mu(L)\) is invariant under the first-return map \(G_\pi\), which is conjugate to a cyclic type and therefore uniquely ergodic. Thus \(\nu\) is normalized Lebesgue measure on \(L\). The disjoint finite towers reconstruct \(\mu\) uniquely from \(\nu\), so \(\mu\) must be Lebesgue measure. This proves uniqueness for all six without asserting that their topological factor structures coincide.

**Step 4: the three return laws.** Conditional Lebesgue measure on \(L\) assigns mass \(1/3\) to each \(J_i\). Thus \(\tau_\pi\) takes the values in the corresponding table triple with multiplicity \(1/3\), and in every case \(\mathbb E\tau_\pi=(h_0+h_1+h_2)/3=4\). The three squared-moment means are \(16\), \(24\), and \(34\), so \(\operatorname{Var}(\tau_\pi)\) is \(0\), \(8\), or \(18\), respectively.

## Verification

The accompanying self-contained `verify_odometer.py` enumerates exactly all six permutations and their 12-state finite transition graphs, checks every listed itinerary and induced permutation, certifies that each row's towers cover the twelve cells exactly once, and checks the renormalization identities using rational arithmetic. Run `python3 verify_odometer.py`; successful execution ends with `EXACT_CELL_GRAPH_OK`. The proof of aperiodicity for infinitely many iterates is the induction in Step 2, **not** finite orbit sampling; uniqueness uses the quoted primary literature as described in Step 3.

## Relationship to prior work

Bruin and Lukina introduced and analyzed rotated odometers. Their *Rotated Odometers* (arXiv:2101.00868, originally public 4 January 2021; journal DOI 10.1112/jlms.12731) gives the generic return-map algorithm (Section 5), the ergodicity criterion (Theorem 1.4), and odometer conjugacy for the two cyclic three-interval permutations (Example 5.16 and Proposition 8.4). Those results are used and credited. The present claim concerns the **complete six-permutation classification**, the explicit transposition reductions, and the three complete return-time laws; it does **not** re-claim the cyclic cases as first discoveries.

Their *Rotated Odometers and Actions on Rooted Trees* (arXiv:2104.05420; DOI 10.4064/fm74-10-2022) concerns partitions into dyadic numbers of equal intervals, which does not encompass the present three-piece case. The importance of the three-piece boundary is also visible by comparison with two pieces: if the two halves are swapped before applying \(\mathfrak a\), every \(x\in[1/2,1)\) is fixed. Hence the aperiodicity of *every* three-piece rearrangement is not a generic property of arbitrary finite permutations.

## Limitations

The theorem is limited to the six permutations of **exactly three equal half-open intervals**; it makes no claim for arbitrary unequal partitions or larger alphabets. The derived return law is for the fixed first-quarter cross-section, not every possible section. Unique invariant probability does not assert that all six maps are topologically conjugate to one another. Source comparison and literature searches cannot definitively exclude an earlier equivalent classification under other terminology. The finite graph checker is not a substitute for the infinite aperiodicity or invariant-measure arguments.

## References

1. H. Bruin and O. Lukina, *Rotated Odometers*, arXiv:2101.00868 (first public version 2021-01-04), Sections 3, 5, 7 and Proposition 8.4; *Journal of the London Mathematical Society* 107 (2023), 1983–2024, DOI: 10.1112/jlms.12731.
2. H. Bruin and O. Lukina, *Rotated Odometers and Actions on Rooted Trees*, arXiv:2104.05420 (first public version 2021-04-12); *Fundamenta Mathematicae* 260 (2023), 233–249, DOI: 10.4064/fm74-10-2022.
