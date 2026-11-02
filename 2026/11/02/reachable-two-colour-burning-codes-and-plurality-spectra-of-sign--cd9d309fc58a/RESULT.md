# Reachable two-colour burning codes and plurality spectra of signed stars

## Finding

Consider the signed star \(\Gamma_\sigma=(K_{1,n},\sigma)\) with one labelled center \(v_0\), labelled leaves \(v_1,\ldots,v_n\), and \(n\ge 3\). Its \(n\) spoke signs are \(\sigma_i\in\{-1,1\}\), and \(q=|\{i:\sigma_i=-1\}|\). Signed burning means the spread-before-ignition, simultaneous two-colour process of Fallat, Gupta, Khodamoradi, and Zilles [1]. Let \(\mathcal R(\Gamma_\sigma)\subseteq\{-1,1\}^{n+1}\) be the set of complete attainable final colourings.

**Theorem (complete signed-star spectrum).** Put \(\phi=(1,\sigma_1,\ldots,\sigma_n)\), and let \(\mathbf{1}\) denote the all-positive word. Define

\[
\mathcal C_n=\{\varepsilon\mathbf{1}:\varepsilon\in\{-1,1\}\}\;\cup\;\{\varepsilon\mathbf{1}\text{ with exactly one leaf coordinate reversed}:\varepsilon\in\{-1,1\}\}.
\]

Then, with coordinatewise multiplication,

\[
\mathcal R(\Gamma_\sigma)=\phi\odot\mathcal C_n,\qquad |\mathcal R(\Gamma_\sigma)|=2(n+1).
\]

The plurality number (maximum number of vertices receiving the same fire colour) depends only on \(q\). Writing

\[
d_n(q)=\min\{\max(0,q-1),\ \max(1,n-q)\},
\]

we have, for every \(0\le q\le n\),

\[
Y(\Gamma_\sigma)=n+1-d_n(q).
\]

Thus the **complete plurality distribution across all \(2^n\) labelled spoke signings** is the polynomial

\[
\mathcal P_n(t)=\sum_{q=0}^{n}\binom nq t^{n+1-d_n(q)}.
\]

Moreover the binary reachable-colouring code \(\mathcal C_n\) has covering radius

\[
\operatorname{cr}(\mathcal C_n)=\rho_n=\max\left\{1,\left\lfloor\frac{n-1}{2}\right\rfloor\right\}.
\]

The signatures minimizing plurality (equivalently, the normalized deep holes of the code) are precisely those whose number of negative spokes belongs to the following set:

\[
\begin{array}{c|c}
 n & q\\ \hline
 3 & 2,3\\
 4 & 2,3,4\\
 n\ge5\text{ odd} & (n+1)/2\\
 n\ge6\text{ even} & n/2,\ n/2+1
\end{array}
\]

Consequently their exact number among edge signings is, respectively, \(4\), \(11\), \(\binom{n}{(n+1)/2}\), and \(\binom{n}{n/2}+\binom{n}{n/2+1}\). The full length-\(n+1\) code has twice as many deep-hole words, because normalization of the center sign identifies a word and its global negation.

## Assumptions and scope

The star is finite, simple, undirected, connected and has a labelled center and labelled leaves; \(n\ge3\). Signs and fire colours belong to \(\{-1,1\}\). Initially all vertices are unburned; in each round, unburned vertices simultaneously adopt the sign of a strict majority of signed influence from already burnt neighbours (ties remain unburned), then one still-unburned vertex may be ignited in either colour. The process stops when all vertices are burnt. The set of attainable complete colourings includes all legal sequences, not only shortest sequences. An all-positive word is \(\mathbf 1\); one exceptional leaf means **one leaf**, never the center, differs from the remaining vertices.

## Proof

**1. All-positive star.** Fix a legal complete burning process on the all-positive star. The first round ignites exactly one vertex since no spread occurs from an empty initial configuration. If the center is ignited first, every leaf inherits the center's colour at the next spread, producing a constant final colouring.

Otherwise a leaf \(v_i\) is ignited first in colour \(\varepsilon\). At the beginning of round two, the center, which has just that one burnt neighbour, acquires colour \(\varepsilon\). The remaining leaves are not adjacent to the initial leaf, so still have no burnt neighbours. The subsequent ignition can choose at most one of these leaves and give it colour \(\varepsilon\) or \(-\varepsilon\). At the third spread, every other leaf receives colour \(\varepsilon\) from the center. Hence no completed colouring differs from its center at more than one leaf.

Conversely, either constant colouring is obtained by igniting the center first. To create a prescribed opposite-coloured exceptional leaf \(v_j\), ignite some other leaf \(v_i\) in colour \(\varepsilon\) in round one, then ignite \(v_j\) in colour \(-\varepsilon\) after the center spreads in round two. This is possible because \(n\ge3\). These cases prove that the reachable-colouring code for the all-positive star is exactly \(\mathcal C_n\). Its \(2(n+1)\) words are distinct, since the center sign and position (or absence) of the exceptional leaf recover the description.

**2. Arbitrary signatures.** Put \(\phi(v_0)=1\) and \(\phi(v_i)=\sigma_i\). Then the given spoke signature equals the all-positive signature switched at exactly the negative leaves. Switching changes each reachable colour \(\nu(v)\) to \(\phi(v)\nu(v)\), by the direct influence identity

\[
\sum_u\sigma(vu)\phi(u)\nu(u)=\phi(v)\sum_u\nu(u)
\]

on star edges, and the oddness of the sign function. This is precisely the signed-burning switching lemma [1, Lemma 2.3]. Therefore \(\mathcal R(\Gamma_\sigma)=\phi\odot\mathcal C_n\).

**3. Exact plurality.** The maximum number of positive vertices in a reachable colouring is the order minus the minimum Hamming distance from \(\phi\) to \(\mathcal C_n\); negating all colours shows that this is the ordinary maximum plurality [1, Proposition 2.9]. Among codewords with positive center, all negative leaves of \(\phi\) are disagreements except that one may be corrected by the exceptional-leaf choice. The minimum distance to this half of the code is \(\max(0,q-1)\). Among codewords with negative center, the center necessarily disagrees and all \(n-q\) positive leaves disagree except that one may be corrected, giving \(1+\max(0,n-q-1)=\max(1,n-q)\). Their minimum is exactly \(d_n(q)\), and hence the plurality formula follows. There are \(\binom nq\) labelled signatures with \(q\) negative spokes, proving the enumerator.

**4. Covering radius and deep holes.** Any length-\(n+1\) word can be negated globally without changing its distance to \(\mathcal C_n\), since the code is closed under global negation. We may therefore normalize its center to \(+1\). Its Hamming weight on the leaf positions is some \(q\), and by the preceding calculation its distance to the code is \(d_n(q)\). Maximizing \(d_n(q)\) for integer \(0\le q\le n\) gives \(\rho_n=\max\{1,\lfloor(n-1)/2\rfloor\}\). For \(n=3\) the maximizing weights are \(2,3\), and for \(n=4\) they are \(2,3,4\). For odd \(n\ge5\) the unique maximizing weight is \((n+1)/2\); for even \(n\ge6\), the two maximizing weights are \(n/2\) and \(n/2+1\). Counting words of each weight proves both the exact signature and full-code deep-hole enumerations. These cases include all boundary values of the theorem.

## Verification

The standalone script `verify_signed_star.py` computes the full state graph of the signed spread-before-ignition process directly, with no use of the switching formula in its state-transition function. It exhausts all \(2^n\) labelled signings for each \(3\le n\le8\), checking every reachable colouring, exact cardinality, plurality value, and resulting distribution. Independently, it checks every possible normalized code distance for each \(9\le n\le15\) against direct Hamming-distance minimization. Run `python3 verify_signed_star.py` with Python 3 standard library. Verified output:

```
VERIFY_OK full_signed_dynamics_star_n=3..8 signings=504 terminal_colorings_checked=8160 direct_code_distances_n=9..15 all_signings
```

The arbitrary-order conclusions rely on the constructive proof above; finite tests only probe its premises and boundary cases.

## Relationship to prior work

Fallat, Gupta, Khodamoradi, and Zilles [1] introduced the signed two-colour process, proved the general switching identity and Hamming-distance/covering-radius interpretation, and investigated signed **paths**. Their complete accessible arXiv HTML manuscript, including its definitions, signed-path results, complexity section and conclusions, was inspected. The general switching/Hamming identities are used here as prior results and are **not** claimed as discoveries. For \(n\ge3\), a star has a degree-at-least-three center and is not one of their path graphs; its exact reachable code, complete signing distribution and deep-hole census are not supplied by their stated results. Their conclusion explicitly proposes extending the parameter to classes of signed trees and studying code covering radii. No equivalent signed-star enumeration was located in targeted mathematical-record and literature searches. This is a qualified priority assessment, not proof of historical uniqueness.

## Limitations

The theorem concerns two colours, labelled signed stars, the original spread-before-ignition process without a deadline, and all complete reachable colourings. It does not determine the code or optimal plurality of arbitrary trees, signed cycles, graph products, or restricted-time games. It counts labelled signings, not isomorphism orbits, and its full-code deep-hole counts distinguish the two possible center signs. No independent audit has been performed; historical priority may be affected by overlooked sources or equivalent coding-theoretic results.

## References

[1] S. Fallat, H. Gupta, K. Khodamoradi, S. Zilles, *Burning Signed Graphs*, arXiv:2610.02506v1, first submitted 2026-10-01. https://arxiv.org/html/2610.02506v1 . Relevant: Definition 2.1, Lemma 2.3, Corollary 2.4, Proposition 2.9, Remark 2.10, Section 3, Section 5.
