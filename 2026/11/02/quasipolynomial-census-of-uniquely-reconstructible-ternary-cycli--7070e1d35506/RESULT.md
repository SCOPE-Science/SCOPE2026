# Quasipolynomial census of uniquely reconstructible ternary cyclic Markov profiles

## Finding

Fix the labeled alphabet \(\Sigma=\{0,1,2\}\). For an indexed circular word \(w=w_0\cdots w_{n-1}\in\Sigma^n\), let
\[
K(w)_{ij}=\#\{r\pmod n:(w_r,w_{r+1})=(i,j)\},\qquad i,j\in\Sigma.
\]
Two words are considered the same circular reconstruction exactly when they differ by a cyclic rotation, **not** by an alphabet permutation or reversal. A realizable matrix \(K\) is *uniquely reconstructible* if all length-\(n\) words with that matrix belong to one rotation class. Write \(U_n\) for the number of distinct such matrices; a matrix is counted once, irrespective of how many indexed words realize it.

**Theorem.** The initial values are \(U_1=3\), \(U_2=6\), \(U_3=11\), \(U_4=24\), and \(U_5=45\). For every integer \(n\ge6\),
\[
U_n=n^2+9n-26+\varepsilon_{n\bmod6},\qquad
(\varepsilon_0,\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4,\varepsilon_5)=(0,7,4,3,4,7).
\]
In particular \(U_n=n^2+O(n)\), and the exact count is a degree-two quasipolynomial of period dividing six. The result includes a structural classification of all uniquely reconstructible matrices, given below.

The first values \(U_1,\ldots,U_{15}\) are
\[
3,6,11,24,45,64,93,114,139,168,201,226,267,300,337.
\]

## Assumptions and scope

All counts are for exactly \(n\) cyclic adjacent *ordered* pairs, including the pair wrapping from the last position to the first. Repeated words and periodic rotation classes are allowed. Matrix entries are nonnegative integers and the three alphabet labels are distinguished. The theorem counts profiles with **one circular realization**, not profiles having exactly one *indexed* realization. No genericity or full-alphabet-use assumption is made.

An admissible matrix has balanced in- and out-degree and connected positive-edge support on its nonisolated vertices. These conditions are necessary and sufficient by the Euler tour criterion. Self-loops count as edges, but zero-degree vertices may be omitted. The proof uses this exact criterion rather than the generally larger set of all balanced integer matrices.

## Proof

**1. Exact necklace count at a fixed profile.** Let \(d_i=\sum_jK_{ij}\) and let \(S=\{i:d_i>0\}\). For a connected balanced matrix, let \(\tau\) be the number of in-arborescences of its off-diagonal directed multigraph rooted at any chosen vertex in \(S\), with multiplicities; for \(|S|=1\), set \(\tau=1\). For a balanced graph \(\tau\) is independent of the root. The BEST theorem, with permutations of identical arcs divided out, gives the following number of *indexed* words having the profile:
\[
W(K)=n\,\frac{\tau\prod_{i\in S}(d_i-1)!}{\prod_{i,j}K_{ij}!}.
\]
Consequently put \(Q(K)=W(K)/n\). If \(N(K)\) denotes the number of circular reconstructions (rotation classes), then \(N(K)\ge Q(K)\), since each rotation class has at most \(n\) indexed representatives. If \(Q(K)>1\), necessarily \(N(K)\ge2\). If \(Q(K)=1\) and the entries of \(K\) have gcd one, every realizing word has full rotation period, whence \(N(K)=1\). The remaining cases with \(Q(K)<1\) are treated explicitly below: they are repetitions of a directed simple cycle.

To justify the exact expression without relying on a black-box numerical computation, the last-exit tree proof of BEST first selects a rooted in-arborescence and orders the remaining exits at each visited vertex. Dividing by \(\prod_{ij}K_{ij}!\) identifies indistinguishable arcs. Summing possible initial symbols supplies the factor \(n\). The same identity also follows from Whittle's exact Markov type-class formula. The tree factor for all three active vertices is the two-by-two directed Laplacian minor.

**2. Flow normal form.** After reversing the alphabet labels if needed, the six off-diagonal entries have the unique form
\[
K_{01}=a+t,\quad K_{10}=a,\quad
K_{12}=b+t,\quad K_{21}=b,\quad
K_{20}=c+t,\quad K_{02}=c,
\]
with \(a,b,c,t\ge0\). The other triangle orientation is obtained by reversing labels; when \(t=0\), the form is counted only once. Denote loops by \(\ell_i=K_{ii}\). For three active vertices, the arborescence factor and off-diagonal outdegrees are
\[
\tau=ab+ac+bc+t(a+b+c)+t^2,\quad
(s_0,s_1,s_2)=(a+c+t,a+b+t,b+c+t).
\]
If \(Q_0\) is the ratio \(Q\) with all loops set to zero, loop insertion changes this ratio by the **exact multiplicative factor**
\[
Q(K)=Q_0\prod_{i\in S}\binom{\ell_i+s_i-1}{s_i-1}
\]
when every positive-degree vertex has \(s_i\ge1\). For a one-vertex profile the result is immediate. The binomial factor is identically one when \(s_i=1\), and strictly increases above one with any loop when \(s_i\ge2\).

**3. Exhaustion of the off-diagonal cases.** The following elementary factorial calculations give all possible singleton circular profiles.

* If only two vertices are active, their reciprocal multiplicities are equal to some \(r\ge1\). The loop-free ratio is \(Q_0=1/r\). For \(r=1\), any loops at the two vertices are allowed. For \(r\ge2\), either both loop counts are zero (the periodic alternating circle), or exactly one loop occurs at either vertex. In the latter case \(Q=1\) and the profile is primitive; any larger loop total has \(Q>1\). A one-vertex profile is always a constant circle.
* When \(t\ge1\), with no reciprocal pairs \(a=b=c=0\), the loop-free ratio is \(1/t\). If \(t=1\), loops at all three vertices are arbitrary. If \(t\ge2\), there may be zero loops or exactly one loop at one vertex; more loops force \(Q>1\).
* When \(t\ge1\) and exactly one reciprocal pair has multiplicity \(a\ge1\) (rename the pair if necessary),
  \[
  Q_0=\frac{(a+t-1)!}{a!t!}.
  \]
  Hence \(Q_0=1\) precisely when \(a=1\) or \(t=1\), and \(Q_0>1\) otherwise. For \(t=1\), arbitrary loops are allowed **only at the vertex outside that reciprocal pair**. For \(t\ge2\) and \(a=1\), no loops are allowed. These admissible matrices all have gcd one.
* When \(t=0\) and precisely two of \(a,b,c\) are positive, write the multiplicities \(a,b\) on the two reciprocal edges sharing a central vertex. Then
  \[
  Q_0=\frac{(a+b-1)!}{a!b!}.
  \]
  This is one exactly when \(\min(a,b)=1\), and is greater than one otherwise. No loops at the central vertex are allowed. If \(a=b=1\), loops at either endpoint are arbitrary. If \(a=1<b\), loops are allowed only at the endpoint of the unit-multiplicity pair, and symmetrically for \(b=1<a\).
* Every other three-vertex pattern has \(Q_0>1\) and cannot be uniquely reconstructible. Indeed, for \(t\ge1\) with at least two positive reciprocal-pair multiplicities, the smallest ratio for fixed \(t\) is \(Q_0(t,1,1,0)=t+1\ge2\); for \(t=0\) with all three multiplicities positive, the smallest ratio is \(Q_0(0,1,1,1)=3\). The needed monotonicity under incrementing any reciprocal-pair multiplicity follows from the explicit factor
  \[
  \frac{Q_0(a+1,b,c,t)}{Q_0(a,b,c,t)}
  =\frac{\tau+b+c+t}{\tau}
  \frac{(a+c+t)(a+b+t)}{(a+t+1)(a+1)}.
  \]
  Cross-multiplication produces a fixed polynomial with nonnegative coefficients after substituting \(t=1+u\), or substituting \(t=0,b=1+u\) when at least two reciprocal pairs are present. This proves the inequality in every relevant nonnegative-integer regime; the fully explicit polynomial sign certificate is reproduced by `verify.py`, using only integer-polynomial addition and multiplication. Symmetry covers increments of \(b\) and \(c\).

For the cases with \(Q_0<1\) (repeated alternating two-cycles or repeated directed triangles), the loop rules just listed are exhaustive from the binomial factor. With no loop the respective repeated simple cycle plainly has one rotation class; with exactly one loop the gcd becomes one and \(Q=1\). All other admitted patterns have gcd one and \(Q=1\), so the lower-bound criterion from Step 1 is also sufficient. This completes the structural characterization, including all periodic exceptions.

**4. Counting the characterized matrices.** For \(n\ge6\), the disjoint families contribute:

| Family | Number of profiles |
|---|---:|
| Constant circles | \(3\) |
| One reciprocal pair, multiplicity one, arbitrary endpoint loops | \(3(n-1)\) |
| A repeated two-cycle, zero loops | \(3\) if \(2\mid n\), otherwise \(0\) |
| A repeated two-cycle, one loop | \(6\) if \(n\) is odd, otherwise \(0\) |
| Unit directed triangle, arbitrary loops | \((n-1)(n-2)\) |
| Unit directed triangle, one positive reciprocal pair, loops at third vertex | \(6\lfloor(n-3)/2\rfloor\) |
| Repeated directed triangle, zero loops | \(2\) if \(n\equiv0\pmod3\), otherwise \(0\) |
| Repeated directed triangle, one loop | \(6\) if \(n\equiv1\pmod3\), otherwise \(0\) |
| Repeated directed triangle plus one reciprocal pair, zero loops | \(6\) if \(n\equiv2\pmod3\), otherwise \(0\) |
| Two unit reciprocal pairs sharing a center, arbitrary endpoint loops | \(3(n-3)\) |
| One unit and one larger reciprocal pair sharing a center, loops only at the unit endpoint | \(6(\lfloor(n-2)/2\rfloor-1)\) |

Summing and separating the six congruence classes proves the displayed quasipolynomial. The five smaller values follow directly from the same classification, with absent repeated-cycle families treated at their natural minimum lengths.

## Verification

`verify.py` independently enumerates every balanced connected ternary transition matrix through length \(25\), computes its exact rotation-orbit number via the BEST formula combined with Burnside's lemma, and checks the above structural criterion and closed formula. It also checks the monotonicity polynomial by exact coefficient arithmetic in two shifted nonnegative-variable regimes. `crosscheck.py` independently enumerates every ternary indexed word through length \(12\), canonically reduces by rotation, groups by adjacent-pair profile and checks the formula without using BEST, the normal form or the classification.

To reproduce: run `python3 verify.py` and `python3 crosscheck.py` in a directory containing the two scripts. Both need only Python's standard library. The expected terminal markers are `VERIFY_OK` and `CROSSCHECK_OK`. The polynomial monotonicity argument and factorial inequalities are the all-length proof; the finite enumerations are cross-checks, not substitutes for that proof.

## Relationship to prior work

Jacquet, Knessl and Szpankowski (2010; expanded 2012) establish the model of cyclic Markov types, exact formulas for the **number of balanced matrices** at ternary alphabet size and asymptotic equivalence to realizable Eulerian profiles. Their expanded work explicitly distinguishes connected realizable profiles from arbitrary balanced matrices and recalls Whittle's type-class count. It does **not** give the number of profiles with exactly one circular-word realization, nor this all-length structural classification and quasipolynomial.

Grisales, Labelle, Posada and Dimitrov (2022) count certain loopless digraphs with one edge-distinguished Eulerian tour as a function of their vertex number. Obscura Acosta and Tomescu (2023/2024) characterize uniqueness of edge-distinguished Eulerian circuits. Neither statement is equivalent to cyclic reconstruction up to rotation with indistinguishable parallel transitions, arbitrary loop multiplicities, exactly three labeled symbols and variable edge count. Standard BEST and Burnside tools are used here, but their general formulas do not themselves evaluate the present all-length profile census.

## Limitations

This result applies only to ternary alphabets, complete cyclic length-two pattern multiplicities, and uniqueness modulo rotation. It does not count profiles with exactly two or more necklaces, reconstruct from noisy observations, or handle higher-order Markov types. The historical priority comparison covers the named primary papers and indexed search records, not every possible historical thesis, unpublished enumeration or table.

## References

1. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), 387–400. DOI: 10.46298/dmtcs.2768. Full text: https://dmtcs.episciences.org/en/articles/2768/download.
2. P. Jacquet, C. Knessl and W. Szpankowski, *Counting Markov Types, Balanced Matrices, and Eulerian Graphs*, IEEE Transactions on Information Theory 58 (2012), 4261–4272. DOI: 10.1109/TIT.2012.2191476. Author manuscript: https://www.cs.purdue.edu/homes/spa/papers/it12-types.pdf.
3. L. Grisales, A. Labelle, R. Posada and S. Dimitrov, *Digraphs With Exactly One Eulerian Tour*, Journal of Integer Sequences 25 (2022), Article 22.3.8. https://cs.uwaterloo.ca/journals/JIS/VOL25/Dimitrov/dim4.pdf.
4. N. Obscura Acosta and A. I. Tomescu, *Simplicity in Eulerian Circuits: Uniqueness and Safety*, Information Processing Letters 183 (2024), 106421. Preprint: https://arxiv.org/abs/2208.08522.
