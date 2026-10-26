# Reachable-colouring code and exact plurality profile of signed stars

## Finding

Let \(\Gamma\) be a signed star \(K_{1,n}\) with centre \(c\), labelled leaves \(u_1,\ldots,u_n\), \(n\geq1\), and spoke signs \(s_i\in\{-1,1\}\). Let \(p=|\{i:s_i=1\}|\) and \(q=n-p\). Use the two-colour signed-burning process of Fallat, Gupta, Khodamoradi and Zilles [1], with synchronous spreading *before* each optional ignition, and immutable burned colours. Write \(\mathcal R(\Gamma)\) for all reachable final configurations in \(\{\pm1\}^{n+1}\), with yellow denoted \(+1\).

**Theorem.** For every \(n\ge2\), the reachable configurations are exactly
\[
\mathcal R(\Gamma)=\bigcup_{a\in\{-1,1\}}\left(\{(a,as_1,\ldots,as_n)\}\cup\{(a,as_1,\ldots,-as_j,\ldots,as_n):1\le j\le n\}\right).
\]
The union is disjoint. Consequently \(|\mathcal R(\Gamma)|=2(n+1)\), and the *yellow-count enumerator* \(F_\Gamma(z)=\sum_{\nu\in\mathcal R(\Gamma)}z^{|\{v:\nu(v)=1\}|}\) is
\[
F_\Gamma(z)=z^{p+1}(1+pz^{-1}+qz)+z^q(1+qz^{-1}+pz).
\]
Here the Laurent notation is only a compact way to write a polynomial; no term has a negative final exponent. The plurality number is
\[
Y(\Gamma)=\max\{p+1+\mathbf{1}_{q>0},\ q+\mathbf{1}_{p>0}\}.
\]
For the one-leaf star \(K_2\), the only reachable final configurations are \((a,as_1)\) for \(a\in\{-1,1\}\). Their enumerator is \(1+z^2\) for a positive edge and \(2z\) for a negative edge; the plurality number is respectively \(2\) or \(1\).

For the all-positive signed star on \(n\) leaves, its binary reachable-colouring code has covering radius
\[
\operatorname{cr}(\mathcal R(K_{1,n}^{+}))=\begin{cases}1,&n=1,2,\\\lfloor(n-1)/2\rfloor,&n\ge3.\end{cases}
\]
In particular, as the signs vary over *every* signing of the same star,
\[
\min_\sigma Y(K_{1,n},\sigma)=\begin{cases}1,&n=1,\\2,&n=2,\\\lceil(n+3)/2\rceil,&n\ge3.\end{cases}
\]
For \(n\ge2\), an all-yellow final configuration exists if and only if at most one spoke is negative.

## Assumptions and scope

Graphs are finite, simple, labelled stars, with all spoke signs fixed before burning. At time zero all vertices are unburned. In each round all unburned vertices update simultaneously according to the sign of the sum of their signed already-burned neighbours; a vertex remains unburned when that sum is zero. After spreading, one still-unburned vertex is ignited with either sign if any remains. Burned vertices never change. Termination occurs when every vertex burns. This is exactly the one-player process of [1, Definition 2.1], not ordinary unsigned burning, the two-player burning game, or a model with ignition preceding spread.

The theorem concerns *all* complete burning sequences, with no deadline or ignition-count cap. The colours \(\pm1\) are named; colour reversal is a symmetry but the two corresponding configurations are counted separately. The polynomial enumerates **distinct final colourings**, not burning sequences. Covering radius uses the ordinary Hamming metric on the \(n+1\) binary vertex coordinates.

## Proof

**Step 1: exhaustive reachability.** If the centre is ignited in round one with colour \(a\), each leaf has exactly one burned neighbour before the spreading step of round two. All leaves therefore burn simultaneously with colours \(as_i\), and the process terminates. This gives the unflipped configuration.

Otherwise, a leaf \(u_i\) is ignited first, with colour \(b\). In round two the centre has only this burned neighbour, so it burns with \(a=s_i b\). No other leaf can burn in that round's spread, since its sole neighbour was unburned at the end of round one. When \(n\ge2\), exactly one other leaf \(u_j\), \(j\neq i\), is then ignited, with arbitrarily chosen colour. In round three all remaining leaves burn with \(as_k\). Since \(b=as_i\), the first leaf always has its canonical colour, and the second ignition may either agree with or reverse its own canonical colour. Thus every final colouring has at most one reversed leaf relative to its centre.

Conversely, for any specified centre colour \(a\) and any specified leaf \(u_j\) to reverse, choose some \(i\neq j\), ignite \(u_i\) with \(as_i\) in round one, and ignite \(u_j\) with \(-as_j\) in round two after the centre spreads. The required configuration results in round three. The unflipped configuration comes from igniting the centre first. Distinct centre colours and distinct reversed-leaf locations give distinct configurations. For \(n=1\), igniting either vertex forces the other to burn in the second round, and there is no second ignition. This proves the complete claimed reachability descriptions.

**Step 2: polynomial and plurality.** For centre colour \(+1\) the canonical colouring has \(p+1\) yellow vertices. Reversing one of its \(p\) positive-spoke leaves loses a yellow vertex; reversing one of its \(q\) negative-spoke leaves gains one. Thus its enumerator contribution is \(z^{p+1}(1+pz^{-1}+qz)\). For centre colour \(-1\), the canonical colouring has \(q\) yellow vertices; reversing a negative leaf loses one, while reversing a positive leaf gains one. This yields \(z^q(1+qz^{-1}+pz)\). Maximizing exponents gives the displayed formula for \(Y\). All-yellow reachability for \(n\ge2\) requires centre \(+1\) and no more than one negative spoke, and this condition is sufficient by the construction.

**Step 3: exact covering radius.** Take all spoke signs positive and fix an arbitrary binary target word. Let \(t\) be its centre colour and let \(k\in\{0,\ldots,n\}\) count leaves whose target colours differ from \(t\). Among reachable words with centre \(t\), the closest has Hamming distance \(d_1(k)=\max\{k-1,0\}\) from the target, since at most one leaf may be reversed. Among reachable words with centre \(-t\), the centre contributes one mismatch and the closest leaf pattern contributes \(\max\{n-k-1,0\}\), hence \(d_2(k)=1+\max\{n-k-1,0\}\). For \(n\ge2\), therefore,
\[
\operatorname{cr}(\mathcal R(K_{1,n}^{+}))=\max_{0\le k\le n}\min\{d_1(k),d_2(k)\}=\max\{1,\lfloor(n-1)/2\rfloor\}.
\]
For \(n=1\), the reachable code is \(\{(+,+),(-,-)\}\) and has covering radius \(1\).

**Step 4: minimizing over all signings.** Every signing of a tree is a vertex switching of the all-positive signing. In the present case, changing the colours of any specified subset of vertices transports reachable configurations bijectively between switched signings: the signed influence at every unburned vertex changes by exactly its switching factor, which commutes with the sign function. Hence maximizing yellow count after switching by a target word \(w\) is equivalent to minimizing Hamming distance from \(w\) to the original reachable code. As every target is a possible switching word, the minimum plurality over all signings is the number of vertices minus the covering radius. (This is also [1, Proposition 2.9 and Remark 2.10].) Substituting the radius just computed proves the final formula. All conclusions hold for each integer \(n\ge1\).

## Verification

The self-contained standard-library program `verify.py` independently simulates the literal synchronous spread-and-ignition process for every signing on stars with \(1\le n\le7\). For each of the \(254\) signings, it enumerates all reachable final configurations, compares their set and yellow-count distribution to the formulas, checks the plurality, and verifies distinct-colouring counts. It independently enumerates all binary targets to measure the code covering radius for each order, and all signings to check the worst plurality. The program prints `VERIFY_OK` on success. The finite checks provide corroboration; Step 1 and the exact Hamming-distance maximization prove the unrestricted statements.

## Relationship to prior work

Fallat, Gupta, Khodamoradi and Zilles [1] introduce signed burning, its reachable-colouring code and plurality number. Their Section 3 determines bounds and exact special cases for signed *paths*, and their Proposition 2.9/Remark 2.10 identify a general switching-class relationship with covering radii. The exact signed-star reachable set, full colour-count enumerator, plurality formula and star-code covering radius established here are a specialization **requiring the additional branching-point reachability classification in Step 1**, not consequences of the path formulas or a numerical covering-radius identity alone. Their concluding research directions explicitly include extending exact results to classes of signed trees. The result is a complete first branching-tree family; it does not claim the definitions or switching correspondence as new.

Classical graph-burning results [2] concern the number of rounds to burn a graph, which does not determine a signed final-colour distribution. The two-player burning game [3] changes the optimization and is likewise distinct.

## Limitations

Only stars are classified. In general signed trees, several active fronts can meet and tie, so the one-reversed-leaf description need not extend. Distinct burning sequences may lead to the same final colouring, and the polynomial counts the latter only. No algorithmic claim is made for arbitrary signed graphs. An equivalent earlier result under a different terminology or in unindexed literature cannot be absolutely excluded. Independent mathematical review has not been performed.

## References

[1] Shaun Fallat, Himanshu Gupta, Kamyar Khodamoradi and Sandra Zilles, *Burning Signed Graphs*, arXiv:2610.02506, first posted 2026-10-01, especially Definition 2.1, Proposition 2.9, Remark 2.10, Section 3 and Section 5. https://arxiv.org/abs/2610.02506

[2] Anthony Bonato, *A survey of graph burning*, Contributions to Discrete Mathematics 16 (2021), 185–197. https://doi.org/10.55016/ojs/cdm.v16i1.71194

[3] Nina Chiarelli, Vesna Iršič, Marko Jakovac, William B. Kinnersley and Mirjana Mikalački, *Burning game*, arXiv:2409.11328 (2024); the two-player variant is not the signed-burning model. https://arxiv.org/abs/2409.11328
