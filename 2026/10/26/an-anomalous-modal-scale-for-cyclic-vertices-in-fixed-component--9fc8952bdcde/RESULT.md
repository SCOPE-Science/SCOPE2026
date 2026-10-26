# An anomalous modal scale for cyclic vertices in fixed-component random mappings

## Finding
Let \(f:[n]\to[n]\) be a uniform random mapping, \(C\) the number of cyclic vertices of its functional digraph, and \(K\) the number of weakly connected components (equivalently, directed cycles). For \(1\le k\le n\), write \(p_{n,k}(c)=\Pr(C=c\mid K=k)\), \(k\le c\le n\), and let \(m_{n,k}\) be any mode of this distribution. Define \(e_j(c)\) to be the degree-\(j\) elementary symmetric polynomial in \(1,1/2,\ldots,1/(c-1)\), with \(e_0(c)=1\).

**Theorem.** For every \(n\ge1\) and \(1\le k\le n\), the positive sequence \(p_{n,k}(k),\ldots,p_{n,k}(n)\) is strictly log-concave at every interior index (and hence has at most two adjacent modes). Its unnormalized weights and adjacent ratios are exactly
\[
w_{n,k}(c)=\frac{(n)_c}{n^c}e_{k-1}(c),\qquad
\frac{w_{n,k}(c+1)}{w_{n,k}(c)}=
\left(1-\frac{c}{n}\right)
\left(1+\frac{e_{k-2}(c)}{c\,e_{k-1}(c)}\right)
\]
for \(k\ge2\) and \(k\le c<n\); for \(k=1\), the last factor is \(1\). For fixed \(k\ge2\), as \(n\to\infty\), *every* modal choice satisfies
\[
\boxed{\frac{m_{n,k}}{\sqrt{n/\log n}}\longrightarrow\sqrt{2(k-1)}.}
\]
For \(k=1\), the unique mode is \(m_{n,1}=1\) for every \(n\).

This modal scale is smaller by a factor of order \(\sqrt{\log n}\) than the classical \(\sqrt n\)-scale of a typical number of cyclic vertices under the same conditioning. The latter distributional scale is a prior result, not an independent novelty claim here.

## Assumptions and scope
All maps \(f:[n]\to[n]\) have probability \(n^{-n}\); self-loops are allowed. A cyclic vertex lies on a directed cycle. Each weak component contains exactly one such cycle. Log-concavity means \(p_{n,k}(c)^2>p_{n,k}(c-1)p_{n,k}(c+1)\) whenever \(k<c<n\); it is vacuous for supports with fewer than three elements. The asymptotic holds with \(k\) fixed, not growing with \(n\). Natural logarithms are used. For \(c=k\), all displayed denominators are strictly positive.

## Proof
**1. Exact conditional weights.** Choose the cyclic set of size \(c\) in \(\binom nc\) ways. For each choice, the permutation of cyclic vertices with exactly \(k\) cycles has \(\left[{c\atop k}\right]\) possibilities (unsigned Stirling number of the first kind). Every other vertex flows along a directed forest toward one of these \(c\) specified roots. The directed matrix-tree theorem, applied to the complete directed graph with loops excluded, gives \(\det(nI_{n-c}-J_{n-c})=c n^{n-c-1}\) such forests when \(c<n\), and one when \(c=n\). Thus for every \(k\le c\le n\),
\[
\Pr(C=c,K=k)=\frac{\binom nc\left[{c\atop k}\right]c n^{n-c-1}}{n^n}=
\frac1n\frac{(n)_c}{n^c}\frac{\left[{c\atop k}\right]}{(c-1)!}
=\frac1n\frac{(n)_c}{n^c}e_{k-1}(c).
\]
The expression with \(c n^{n-c-1}\) also equals one at \(c=n\). The final equality follows from
\[\prod_{i=0}^{c-1}(x+i)= (c-1)!x\prod_{i=1}^{c-1}\left(1+\frac{x}{i}\right)\]
and coefficient extraction. Conditioning on \(K=k\) leaves weights \(w_{n,k}(c)\). Adjoining the reciprocal \(1/c\) to the alphabet gives \(e_j(c+1)=e_j(c)+e_{j-1}(c)/c\) and hence the asserted ratios.

**2. Strict log-concavity.** Put \(j=k-1\ge1\) and \(r_j(c)=e_{j-1}(c)/e_j(c)>0\). Upon adjoining any positive variable \(a\),
\[
\frac{e_{j-1}+a e_{j-2}}{e_j+a e_{j-1}}-\frac{e_{j-1}}{e_j}
=\frac{a(e_{j-2}e_j-e_{j-1}^2)}{e_j(e_j+a e_{j-1})}\le0,
\]
by the elementary-symmetric Newton inequality; use \(e_{-1}=0\) when \(j=1\). Therefore \(r_j(c)\) is nonincreasing in \(c\), whereas \(r_j(c)/c\) is strictly decreasing. The factor \(1-c/n\) also strictly decreases on \(c<n\). Their positive product \(w(c+1)/w(c)\) is strictly decreasing. When \(k=1\), the ratio is simply \(1-c/n\), again strictly decreasing. Decreasing adjacent ratios are precisely strict log-concavity and imply at most two adjacent maximizers.

**3. Modal scale.** For each fixed \(j\ge1\), set \(H(c)=\sum_{r=1}^{c-1}1/r\). As \(c\to\infty\), the boundedness of \(\sum_{r\ge1}1/r^2\) and expansion of \(\prod_{r<c}(1+x/r)\) imply
\[
e_j(c)=\frac{H(c)^j}{j!}\left(1+O_j(H(c)^{-2})\right),\qquad
\frac{e_{j-1}(c)}{e_j(c)}=\frac{j}{H(c)}(1+o(1)).
\]
For any fixed \(\alpha>0\), choose \(c_n=\lfloor\alpha\sqrt{n/\log n}\rfloor\). Then \(H(c_n)\sim(\log n)/2\). Substituting into the adjacent ratio, retaining its cross term, gives
\[
\sqrt{n\log n}\left(\frac{w_{n,k}(c_n+1)}{w_{n,k}(c_n)}-1\right)
\longrightarrow -\alpha+\frac{2j}{\alpha}.
\]
This limit is positive below \(\sqrt{2j}\) and negative above it. By monotonicity of all adjacent ratios, every mode lies between the corresponding lower and upper comparison indices (up to one index), for every pair of constants straddling \(\sqrt{2j}\). Letting the constants approach this threshold gives \(m_{n,k}/\sqrt{n/\log n}\to\sqrt{2j}\). For \(k=1\), the exact ratio is always less than one, so the mode is at \(c=1\). This completes the proof.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3 and its standard library. It independently enumerates all mappings through five vertices, matches joint \((C,K)\) counts to the forest/Stirling formula, checks elementary-symmetric identities and exact strict adjacent-ratio inequalities for \(2\le n\le50\) using rational arithmetic, and performs nonproof numerical smoke checks of the modal scale. The verifier's result was: `PASS 62604 exact/analytic-identity assertions plus numerical mode smoke checks`. The infinite-domain claims are established by the preceding proof, not by this finite verification.

## Relationship to prior work
Pavlov (1986), Theorem 6 in the accessible detailed abstract, **already proves** a local half-normal law for cyclic vertices of mappings with a fixed (or sufficiently slowly growing) number of components. It does not follow from that fixed-positive-scaled-location local limit that the unscaled mode is of order \(\sqrt{n/\log n}\): the modal region lies at a rescaled location tending to zero, outside the theorem's uniformity window. No claim of novelty is made for Pavlov's half-normal law. Hansen and Jaworski (2006), Corollary 1 and its proof, already supply the Stirling mixture associated with the numbers of cyclic vertices and components. The exact weights here are a specialization and rewriting of that established enumeration. The asserted additional information is **strict finite-sample log-concavity and the distinct modal asymptotic**. Flajolet and Odlyzko (1990) broadly study random mapping statistics, and Kupka (1990) examines the component-count marginal; a more encompassing result could conceivably imply parts of the present finding.

## Limitations
The theorem assumes a uniform mapping and fixed component count. The available detailed abstract of Pavlov supplies its Theorem 6 but not every page of its full text; the author-hosted older Flajolet–Odlyzko version and institutional copy were also not accessible in full. Therefore historical priority of the modal conclusion remains a genuine risk for independent review. Strict log-concavity of known weights uses a standard Newton inequality; that fact by itself is not presented as a major advance. The asymptotic gives leading modal scale but does not classify exact finite-sample ties or higher-order shifts.

## References
1. Yu. L. Pavlov, “Random mappings with constraints on the number of cycles,” *Trudy Mat. Inst. Steklova* **177** (1986), 122–132; English translation *Proc. Steklov Inst. Math.* **177** (1988), 131–142. https://www.mathnet.ru/eng/tm2116 (detailed abstract including Theorem 6).
2. J. C. Hansen and J. Jaworski, “A new random mapping model,” arXiv:math/0603529v1, March 22, 2006, especially Corollary 1. https://arxiv.org/pdf/math/0603529 .
3. P. Flajolet and A. M. Odlyzko, “Random Mapping Statistics,” *EUROCRYPT 1989*, LNCS 434 (1990), 329–354. https://doi.org/10.1007/3-540-46885-4_34 .
4. J. Kupka, “The distribution and moments of the number of components of a random function,” *J. Appl. Probab.* **27** (1990), 202–207. https://doi.org/10.2307/3214607 .
