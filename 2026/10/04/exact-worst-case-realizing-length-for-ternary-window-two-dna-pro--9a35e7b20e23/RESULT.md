# Exact worst-case realizing length for ternary window-two DNA profile rankings
## Finding
Let \(\Sigma=\{0,1,2\}\), and for a circular string let \(p_{ij}\) denote the number of cyclic occurrences of the length-two substring \(ij\). For a feasible strict ranking \(\pi\) of the nine entries \(p_{ij}\), let \(\operatorname{len}(\pi)\) be the shortest circular-string length realizing that ranking. Then
\[
\max_{\pi\ \mathrm{feasible}}\operatorname{len}(\pi)=86.
\]
Exactly \(72\) of the known \(30240\) feasible rankings attain this maximum. One canonical extremal ranking, written from smallest to largest profile entry, is
\[
p_{10}<p_{01}<p_{02}<p_{21}<p_{20}<p_{00}<p_{11}<p_{22}<p_{12}.
\]
It is realized at length \(86\) by the balanced profile matrix
\[
P=\begin{pmatrix}
12&5&6\\
0&13&15\\
11&10&14
\end{pmatrix}.
\]

## Assumptions and scope
The setting is the circular rank-modulation DNA-profile model for alphabet size \(q=3\) and window length \(\ell=2\). Rankings are strict, so all nine profile counts are distinct nonnegative integers. The length of a circular realization equals the sum of its nine length-two profile counts. The result concerns the worst shortest realization over all feasible strict rankings; it does not concern decoding distance, weak rankings with ties, or larger alphabet/window parameters.

## Proof
Flow conservation at the three symbols gives
\[
p_{01}-p_{10}=p_{20}-p_{02}=p_{12}-p_{21}=t.
\]
For a strict ranking \(t\neq0\). After possibly reversing all three ordered pairs, write their low/high entries as \((L_i,H_i)\) with \(H_i=L_i+t\) and \(t>0\). Relabel the three pairs so that \(L_1<L_2<L_3\). Then also \(H_1<H_2<H_3\). Thus the six non-loop positions are one of the five linear extensions
\[
LLLHHH,\quad LLHLHH,\quad LLHHLH,\quad LHLLHH,\quad LHLHLH.
\]
The three loop entries are balance-neutral. Consequently every feasible ranking belongs to one of \(5\binom93=420\) length-relevant shape classes, after forgetting the two orientations, the order labels of the three edge pairs, and the labels of the three loops. These forgotten choices preserve minimum realizing length and contribute \(2\cdot3!\cdot3!=72\) rankings per shape.

For a fixed shape and fixed positive integer \(t\), substitute \(H_i=L_i+t\). Each adjacent rank inequality becomes a lower-bound difference constraint among the six variables
\[
L_1,L_2,L_3,p_{00},p_{11},p_{22}.
\]
The componentwise least nonnegative solution is obtained by longest-path closure of these constraints whenever there is no positive cycle; because every coefficient in the length objective is positive, this least solution minimizes the total length for that fixed \(t\). The exact verifier performs this closure for every one of the \(420\) shapes and every \(1\le t\le28\). It finds a realization of length at most \(86\) for every shape. Values \(t\ge29\) cannot improve such a realization, since the three high-minus-low gaps alone contribute \(3t\ge87\) to the total profile sum. Hence the finite calculation gives the exact minimum length of every shape, not merely an upper bound.

The unique worst shape is
\[
L_1,H_1,L_2,L_3,H_2,p_{00},p_{11},p_{22},H_3.
\]
It has minimum \(86\). This lower bound also has a direct proof. Write \(L_1=a\), \(L_2=b\), and \(L_3=c\). The extremal order requires
\[
a<a+t<b<c<b+t<p_{00}<p_{11}<p_{22}<c+t.
\]
Fitting three distinct loop counts strictly between \(b+t\) and \(c+t\) forces \(c-b\ge4\). The inequality \(c<b+t\) then forces \(t\ge5\). Therefore
\[
a\ge0,\qquad b\ge a+t+1\ge6,\qquad c\ge b+4\ge10,
\]
and the three loop entries are at least \(12,13,14\). The smallest possible ordered profile values are consequently
\[
0,5,6,10,11,12,13,14,15,
\]
whose sum is \(86\). The displayed matrix attains all these bounds and is balanced, so the lower bound is sharp.

Because a strict nonnegative \(3\times3\) profile has at most one zero entry, its nonzero directed support is strongly connected. A balanced integral profile therefore has an Eulerian circuit, which yields a circular string of length equal to its profile sum. This proves that the matrix above genuinely realizes the canonical extremal ranking at length \(86\).

## Verification
The standalone verifier uses only exact integer arithmetic and the Python standard library. It enumerates all \(420\) shape classes, solves each fixed-gap problem by difference-constraint closure, proves that every shape has an optimum at most \(86\), and uses \(3t\ge87\) to exclude every unsearched \(t\ge29\). It finds a unique extremal shape and hence exactly \(72\) extremal full rankings. For the canonical extremizer it checks the displayed matrix entry by entry, verifies equality of row and column sums, constructs an Eulerian circuit, and confirms circuit length \(86\). Replay terminates with `VERIFY_OK`.

## Relationship to prior work
Raviv, Schwartz, and Yaakobi defined \(\operatorname{len}(\pi)\) as the shortest realizing-string length for a feasible permutation and explicitly described this quantity as practically important. For their \(q=3,\ell=2\) base repository of all \(30240\) feasible rankings, they reported only a computer-derived bound \(c_3\le16\) on the maximum profile entry of chosen representatives. Together with their general argument this gives a coarse length bound, not the exact worst shortest length. Their feasibility lemma implies the balance reduction used above; that reduction is prior work and is not claimed as new.

Beeri and Schwartz later improved constructions and realizing lengths for broader code families, but the inspected text does not give the exact worst shortest realization over all \(30240\) ternary window-two rankings. Two 2026 papers specifically revisit enumeration and structural/distance properties of feasible rank-modulation permutations; available metadata was inspected, but full text could not be lawfully retrieved during this run. Their titles and available descriptions concern enumeration, structure, and permutation distance rather than the shortest-string invariant, so they are recorded as residual comparison risk rather than treated as evidence of coverage.

## Limitations
The theorem is specific to strict circular ternary length-two profile rankings. It does not classify shortest realizations for each labeled ranking individually in closed form, optimize non-circular representations, or extend the value \(86\) to larger alphabets or window lengths. The two highly relevant 2026 papers noted above were not fully inspectable, so an unobserved exact shortest-length result in them remains a residual originality risk.

## References
1. N. Raviv, M. Schwartz, and E. Yaakobi, “Rank-Modulation Codes for DNA Storage With Shotgun Sequencing,” *IEEE Transactions on Information Theory* 65(1), 50–64, 2019. First public arXiv version: arXiv:1708.02146v1, 2017-08-07. DOI: 10.1109/TIT.2018.2829876.
2. N. Beeri and M. Schwartz, “Improved Rank-Modulation Codes for DNA Storage With Shotgun Sequencing,” *IEEE Transactions on Information Theory* 68(6), 3719–3730, 2022. arXiv:2101.06033. DOI: 10.1109/TIT.2022.3152392.
3. R. Sobhani, F. Parvaresh, A. Abdollahi, F. Abedi, J. Bagherian, and M. Khatami, “On Enumerating Feasible Permutations for Rank Modulation Codes in DNA Storage via Hyperplane Arrangements,” *IEEE Transactions on Information Theory* 72(8), 5490–5500, 2026. DOI: 10.1109/TIT.2026.3698044.
4. A. Abdollahi, J. Bagherian, F. Jafari, M. Khatami, A. Orak, F. Parvaresh, and R. Sobhani, “Rank-modulation codes for DNA storage in shotgun sequencing: Structure and distance properties,” *Discrete Mathematics* 349(11), 115253, 2026. DOI: 10.1016/j.disc.2026.115253.
