# Composition-resolved cyclic binary three-gram profiles and their sharp saturation threshold

## Finding

For every integer \(n\ge1\) and \(0\le w\le n\), let \(C_{n,w}\) count the *distinct ordered, multiplicity-preserving cyclic three-gram profiles* of binary words of length \(n\) and Hamming weight \(w\). The exact bivariate enumerator, simultaneously resolving block length and symbol composition, is
\[
\begin{aligned}
G(z,u)&=\sum_{n\ge1}\sum_{w=0}^{n} C_{n,w}z^nu^w\\
&=\frac{z}{1-z}+\frac{zu}{1-zu}+\frac{z^2u}{1-z^2u}\\
&\quad+\frac{z^3u}{(1-z)(1-z^2u)(1-z^3u)}
+\frac{z^3u^2}{(1-zu)(1-z^2u)(1-z^3u^2)}\\
&\quad+\frac{1}{(1-z)(1-zu)(1-z^2u)(1-z^4u^2)}
\left(\frac{z^4u^2}{1-z^3u}+\frac{z^7u^4}{1-z^3u^2}\right).
\end{aligned}
\]
Every coefficient is therefore a finite, exact integer; no asymptotic approximation or numerical fitting is involved. Complementing all bits implies \(C_{n,w}=C_{n,n-w}\).

For every integer \(w\ge2\), there is a sharp **composition-fixed length saturation**:
\[
C_{n,w}=S_w=\begin{cases}
(w^3+8w)/8,&w\text{ even},\\
(w^3+7w)/8,&w\text{ odd}
\end{cases}\quad(n\ge3w),
\qquad C_{3w-1,w}=S_w-1.
\]
Thus \(3w\) is the *least* length after which the capacity stabilizes permanently at \(S_w\). The exceptional weights are \(C_{n,0}=1\) for every \(n\ge1\), and \(C_{n,1}=1\) for every \(n\ge1\). The stable-count generating function is
\[
\sum_{w\ge0}S_wu^w
=1+\frac{u}{(1-u)^2}+\frac{u^2}{(1-u)^3(1-u^2)}
+\frac{u^4}{(1-u)^2(1-u^2)^2},
\]
where the \(w=0\) term equals one. For instance, at weight four the capacity first reaches twelve at length twelve, while at length eleven it is eleven.

These are exact *constant-composition zero-error code capacities*: from each distinct three-gram profile, one can choose one source word, while no two sources with the same profile may both belong to a uniquely decodable code.

## Assumptions and scope

All words are indexed binary strings \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\). Indices in the length-three reads are interpreted modulo \(n\), including repeated positions for \(n=1,2\). The observation is the eight-component vector
\[
N_{abc}(x)=\left|\{i\in\mathbb Z/n\mathbb Z:(x_i,x_{i+1},x_{i+2})=(a,b,c)\}\right|,
\quad(a,b,c)\in\{0,1\}^3.
\]
The ordering of reads is lost but individual three-bit read orientation and all multiplicities are retained. Word rotations need not be counted as separate output profiles. Hamming weight is the number of ones in the source word. All identities are formal-power-series identities over \(\mathbb Q[u][[z]]\), with \(G\) interpreted around \(z=0\).

## Proof

**1. Exact circulation and realization.** Form the order-two binary de Bruijn directed graph: a three-gram \(abc\) is the directed edge \(ab\to bc\). Cyclic read counts are nonnegative integer edge multiplicities. Their support, after removing isolated vertices, is connected, and at every vertex incoming and outgoing multiplicities are equal. Conversely, any nonzero balanced directed multigraph with connected positive-edge support has an Eulerian circuit, yielding a cyclic source word and exactly the prescribed counts. This argument holds at all lengths, including one and two.

Put
\[
a=N_{000},\quad b=N_{001}=N_{100},\quad d=N_{011}=N_{110},
\quad f=N_{101},\quad h=N_{111},\quad c=N_{010}=b+f-d.
\]
The equalities follow from flow balance at vertices \(00,11,01,10\). The exact constraints are \(a,b,d,f,h\ge0\), \(c=b+f-d\ge0\), and
\[
n=a+h+3b+d+2f,\qquad w=b+d+f+h.
\]

**2. Connected-support partition.** There are five disjoint possibilities, and the following entries are *exact* bivariate generating functions, where \(z\) records length and \(u\) records weight:

| Case | Required parameters and restrictions | Contribution |
|---|---|---|
| I | \(b,d>0\), \(f\ge\max(0,d-b)\), \(a,h\ge0\) | \(\displaystyle\frac{z^4u^2/(1-z^3u)+z^7u^4/(1-z^3u^2)}{(1-z)(1-zu)(1-z^2u)(1-z^4u^2)}\) |
| II | \(b>0,d=h=0\), \(f,a\ge0\) | \(\displaystyle\frac{z^3u}{(1-z)(1-z^2u)(1-z^3u)}\) |
| III | \(b=a=0,d>0,f\ge d,h\ge0\) | \(\displaystyle\frac{z^3u^2}{(1-zu)(1-z^2u)(1-z^3u^2)}\) |
| IV | \(b=d=a=h=0,f>0\) | \(\displaystyle\frac{z^2u}{1-z^2u}\) |
| V | A single constant loop at \(00\) or \(11\), of positive multiplicity | \(\displaystyle\frac{z}{1-z}+\frac{zu}{1-zu}\) |

The parameter restrictions are exactly the connected-support possibilities: when both bridge counts are positive, all active edges meet one connected component; with exactly one bridge, the loop at the opposite constant vertex is forbidden; without bridges, only a two-cycle or a single constant loop remains. No disconnected balanced edge vector is accidentally included. For case I, write \(b=d+t\) with \(t\ge0\) and free \(f\ge0\), or \(d=b+t\) with \(t\ge1\) and \(f=t+s\), \(s\ge0\). The two summands arise from these disjoint possibilities; all variables contribute independent geometric series. Summing cases I–V gives the displayed \(G(z,u)\).

**3. Sharp fixed-weight stabilization.** For fixed \(w\ge2\), in cases I and II the loop count \(a\) has weight zero. Each choice of the other parameters with total weight \(w\) therefore determines a *single* profile at every length \(n\) no smaller than its minimum \(n_0\), by setting \(a=n-n_0\). In case I,
\[
3w-n_0=2d+f+2h\ge2;
\]
in case II, \(b+f=w\) and \(n_0=3b+2f=2w+b\le3w\), with equality exactly for \(b=w,f=0\). Case III has \(n=w+f\le2w-1\), case IV has \(n=2w\), and case V cannot occur for \(n\ge3w-1\). Hence for \(n\ge3w\) the attainable profiles consist precisely of all the case I and II parameter assignments of weight \(w\), and at \(n=3w-1\) the sole missing assignment is \(b=w,f=0\). This proves both stabilization and its sharpness.

For these stable parameter assignments, discard the \(a\) factor and retain the weight variable. Case II contributes \(u/(1-u)^2\). Case I contributes
\[
\frac{u^2}{(1-u)^3(1-u^2)}+\frac{u^4}{(1-u)^2(1-u^2)^2}.
\]
Include the single all-zero profile for \(w=0\). The resulting stable generating function simplifies to
\[
\frac{u^6-u^5+3u^3-u+1}{(1-u)^4(1+u)^2},
\]
whose even- and odd-degree coefficients give the stated \(S_w\). For \(w=1\), there is exactly one cyclic rotation class of a single one at every length; for \(w=0\), only the all-zero word occurs. Complementation proves the asserted fixed-length weight symmetry.

## Verification

The standalone Python 3 standard-library program `verify.py` recomputes the full ordered profiles from all \(2^n\) literal binary sources for each \(1\le n\le16\), aggregates their weights independently, and compares them to the connected-circulation parameter enumeration. It further checks the prior known total-length rational generating function against the weighted sum of independently enumerated parameters for every length through 42, and the sharp saturation identities for each weight from 2 through 24. Run `python3 verify.py` in the directory containing this document and the verifier. The exact results printed by the script form finite reproducibility checks; the infinite statements are proved in the preceding steps, not inferred from numerical tests.

The first sixteen total profile counts (summing over all weights), used only as a consistency check against the previously recorded unweighted calculation, are \(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271\).

## Relationship to prior work

Kiah, Puleo and Milenkovic [1] set out a general de Bruijn-flow framework for DNA sequence profiles, including order-of-growth statements, but their inspected discussion and numerical table do not give this exact bivariate fixed-weight count or its sharp saturation threshold. Chang, Chrisnata, Ezerman and Kiah [2] address different linear finite-length profile regimes and bounds. Yehezkeally and Polyanskii [3] investigate the noisy substring channel and constrained reconstruction coding, which motivates composition-aware exact capacities, not this circular enumeration.

An existing exact count of *all* unrestricted cyclic binary three-gram profiles \(C_n\), without Hamming-weight resolution, is already available. **That univariate count, its period and its asymptotic are not claimed as new here.** A separate restricted enumeration forbidding cyclic `111` gives an earlier weight-resolved count and a similar saturation cutoff in a *proper restricted language*. It does not determine all unrestricted composition classes: sources with repeated ones and with the `111` edge and both bridge types are present in the present enumeration, and the new rational terms are essential. The contribution here is the complete exact bivariate composition refinement and the corresponding unrestricted sharp fixed-weight law.

## Limitations

This is a noiseless, single-read-length, binary, *cyclic* and position-unlabeled observation model; it does not address unknown read deletions or substitutions, arbitrary alphabet sizes, or individual fiber multiplicities. The resulting source-profile enumeration is exact, but no independent audit has been performed. A full-text inspection of Jacquet, Knessl and Szpankowski's 2012 Markov-type enumeration paper was not possible: its abstract and the accessible discussion in [1] concern asymptotic enumeration, but the possibility of an overlooked exact fixed-composition formula is a residual priority risk. Analogous exact tables under other terminology may also exist.

## References

[1] H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (first public 2015-02-02), https://arxiv.org/abs/1502.00517 .

[2] E. Chang, D. Chrisnata, M. F. Ezerman, and H. M. Kiah, *Rates of DNA Sequence Profiles for Practical Values of Read Lengths*, arXiv:1607.02279 (first public 2016-07-08), https://arxiv.org/abs/1607.02279 .

[3] A. Yehezkeally and N. Polyanskii, *On Codes for the Noisy Substring Channel*, arXiv:2102.01412 (first public 2021-02-02), https://arxiv.org/abs/2102.01412 .

[4] P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), DOI:10.1109/TIT.2012.2191476 .
