# Polynomial discrepancy ladders in primitive automatic subshifts

## Finding

For every pair of integers \(r\ge1\) and \(d\ge1\), an explicit primitive aperiodic constant-length substitution produces a sharp two-parameter hierarchy of nonconstant arithmetic progressions. Its length is \(k=r+2\), its alphabet is \(\mathcal A=\{0,1,\ldots,d+1\}\), and its rule is
\[
\varphi(a)=\underbrace{aa\cdots a}_{r\text{ copies}}\,g(a)\,0,
\qquad g(a)=\min\{a+1,d+1\}.
\]
Let \(x\in\mathcal A^{\mathbb Z}\) be the substitution-fixed sequence anchored with the neighboring symbols \(x_{-1}=x_0=0\). Let \(D_m\) be the number of residues \(0\le i<k^m\) for which the full two-sided progression \(\big(x_{i+nk^m}\big)_{n\in\mathbb Z}\) is nonconstant. Then, **exactly for every integer \(m\ge0\)**,
\[
\boxed{D_m=\sum_{j=0}^{\min\{d,m\}}\binom mj r^{m-j}}.
\]
Consequently \(D_m\sim m^d r^{m-d}/d!\). The number \(K_m\) of distinct full progression sequences at depth \(m\), counting constant and nonconstant sequences, is also exact:
\[
\boxed{K_m=\begin{cases}1,&m=0,\\2m+1,&1\le m\le d,\\2d+3,&m\ge d+1.\end{cases}}
\]
The complete \(k\)-kernel therefore consists of exactly \(2d+3\) sequences. Its nonconstant members are \(g^j\circ x\) for \(0\le j\le d\), and its constant members are the \(d+2\) constant sequences with values in \(\mathcal A\).

The discrepancy spectral radius is exactly \(r\). Applying the *published* general characterization of Gröger and Krawczyk therefore gives
\[
\mathrm{ac}(X_{\varphi})=\frac{\log(r+2)}{\log((r+2)/r)},
\]
and the minimal infinite substitution subshift \(X_\varphi\) is both tame and null **if and only if** \(r=1\). In particular, the same amorphic complexity \(1\) permits every polynomial exponent \(d\ge1\) in the exact finite-scale nonconstant-progression count. The general tame/null characterization and amorphic-complexity formula are known; the asserted specialization is the explicit full-degree realization and its exact progression and kernel formulas.

## Assumptions and scope

All parameters \(r,d\) are positive integers, with the symbolic alphabet, morphism, and bi-infinite fixed point defined above. The right half of \(x\) is the limit of \(\varphi^m(0)\), and its left half is the corresponding left-prolongable limit because every substituted word ends with \(0\). The common boundary is chosen between two zeros. The subshift \(X_\varphi\) is the orbit closure of this two-sided \(x\) under the left shift. The progression index \(n\) ranges over **all** integers, not only a finite sample; \(m\) starts at zero. The \(k\)-kernel means the set of distinct sequences \(\big(x_{i+nk^m}\big)_{n\in\mathbb Z}\) as \(m\ge0\) and \(0\le i<k^m\) vary. Amorphic complexity, tameness, and nullness have their standard topological-dynamical meanings in the cited papers.

## Proof

**1. Primitivity, height and aperiodicity.** Every \(\varphi(a)\) includes the symbol \(0\), and every iteration of the \(0\)-word exposes one additional symbol under \(g\). Thus a common power, for instance \(\varphi^{d+2}\), contains every letter in the image of every letter: the substitution is primitive. Its fixed point therefore contains all letters on each side and has a minimal orbit closure. The consecutive blocks \(\varphi(g(0))\varphi(0)\) occur in \(\varphi^2(0)\); the former ends and the latter begins with \(0\). Hence two occurrences of \(0\) are adjacent and the substitution has height one.

We will show \(D_m>0\) and \(D_m/k^m\to0\); these imply aperiodicity directly. Suppose that \(x\) has some finite period \(t\). For sufficiently large \(m\), the integer \(h=\gcd(t,k^m)\) is independent of \(m\). Every progression of step \(k^m\) traverses exactly one coset modulo \(h\) in the period-\(t\) word. Consequently the proportion \(D_m/k^m\) equals the fixed fraction of residue classes modulo \(h\) on which the word is not constant; it cannot tend to zero unless eventually \(D_m=0\), contradicting the exact positive formula below. Thus \(X_\varphi\) is infinite and aperiodic.

**2. Exhaustive column semigroup.** The \(k\) column functions of \(\varphi\) are exactly \(r\) copies of the identity \(I\), one successor \(g\), and one reset \(c_0\) to zero. A column of \(\varphi^m\) is a composition of exactly \(m\) such functions, one for each base-\(k\) digit. Without a reset, a composition with \(j\) successors is \(g^j\). For \(0\le j\le d\), this map is nonconstant since its values at \(0\) and \(d+1\) differ; for \(j\ge d+1\), it is identically \(d+1\). Any composition that contains a reset is constant. Therefore a depth-\(m\) column is nonconstant **if and only if** it chooses at most \(d\) successor digits and no reset digits. Selecting their positions and the \(r\) identity-digit choices at all other positions yields exactly
\[
D_m=\sum_{j=0}^{\min(d,m)}\binom mj r^{m-j}.
\]
The identity \(\varphi^m(x)=x\) gives \(x_{i+nk^m}=\varphi^m_i(x_n)\) for every \(n\in\mathbb Z\). Since \(x\) uses every symbol, a column progression is nonconstant exactly when the column function is, and distinct column functions induce distinct sequences. This validates the exact progression count rather than merely counting formal functions.

**3. Full finite-depth kernel.** There are \(\min(d,m)+1\) distinct nonconstant column maps \(I,g,\ldots,g^{\min(d,m)}\). For \(1\le m\le d\), the constant columns are exactly \(c_0,c_1,\ldots,c_{m-1}\), where \(c_j\) denotes the constant map with value \(j\): a reset followed by \(j\) successors realizes each, and \(m\) available digits cannot reach any larger constant. For \(m\ge d+1\), every \(c_0,\ldots,c_d\) is realized by a reset and successors, while the all-successor column realizes \(c_{d+1}=g^{d+1}\). Thus there are \(d+2\) constant types at those depths. Adding the two counts yields the stated exact piecewise formula for \(K_m\) and the complete kernel of size \(2d+3\).

**4. Sharp growth and dynamical classification.** For fixed \(r,d\), the summand with \(j=d\) dominates the finite binomial sum as \(m\to\infty\); hence \(D_m\sim r^{m-d}m^d/d!\). Since \(k=r+2>r\), this establishes \(D_m/k^m\to0\), completing Step 1. On the unordered unequal-letter pairs, every identity column preserves the pair \(r\) times, the reset removes it, and the successor sends it to the successor pair or removes it once the entries coincide. Consecutive successor transitions die after at most \(d+1\) applications. The discrepancy incidence operator is therefore \(rI+N\) with nilpotent \(N\), so its spectral radius is precisely \(r\). The Gröger–Krawczyk Theorems A and B apply to this primitive infinite system and give the stated amorphic-complexity formula and the equivalence of nullness, tameness and \(r=1\). These are applications of their theorems, not replacements for them.

## Verification

The separate standard-library Python program `verify.py` reconstructs every formal column and independently compares it with actual iterated substitution words for sampled parameters. It also checks primitivity witnesses, the adjacent-zero height witness, every exact count \(D_m\) and \(K_m\) in its tested ranges, and the binomial recurrence. Its run yielded **1,822 passed integer assertions** (\(1\le r\le3\), \(1\le d\le5\), \(0\le m\le7\) for the main column tests, plus broader recurrence tests). The proof is universal; finite diagnostics are not an exhaustive proof. Reproduce with `python3 verify.py` after extracting that file from the package.

## Relationship to prior work

Gröger and Krawczyk's 2026 paper establishes the general formula for amorphic complexity and the null/tame characterization (Theorems A and B); its Proposition 5.6 gives an order-of-growth law \(\Theta(m^{d_s}\lambda_s^m)\) for any primitive height-one substitution. Its Example 5.3 evaluates a particular linear-growth progression profile. Those general results and its linear example are **prior knowledge**. The present contribution is a uniform **two-parameter explicit realization** of all positive polynomial exponents and arbitrary positive integer discrepancy bases, plus exact binomial counts at every depth and complete closed finite-kernel counts. The earlier general theorem can predict an asymptotic growth type once the new family's discrepancy matrix is supplied, but does not itself state this family or its exact depth-by-depth formulas.

Fuhrmann and Gröger (2019/2020) develop geometric bounds and formulas for amorphic complexity of constant-length substitutions; their method does not provide the asserted complete explicit two-parameter progression hierarchy. These distinctions concern mathematical statements, not a guarantee that an equivalent earlier construction is absent from all literature.

## Limitations

The result concerns the stated explicit primitive substitution family and its fixed point, not arbitrary automatic sequences. Counts are for progressions at depths equal to powers of \(k=r+2\), not for every step length. The dynamical nullness/tameness assertions rely on the correctly cited published characterization. No quantitative convergence rate for amorphic complexity is asserted. Exhaustive historical priority and independent manuscript assessment have not been performed; a differently named reset-counter substitution may encode the same exact family. The finite verifier does not prove any infinite statement by itself.

## References

1. M. Gröger and E. Krawczyk, *Tameness, nullness, and amorphic complexity of automatic systems*, arXiv:2602.23267, first version publicly posted 26 February 2026; Theorems A/B, Example 5.3 and Proposition 5.6. https://arxiv.org/html/2602.23267
2. G. Fuhrmann and M. Gröger, *Constant length substitutions, iterated function systems and amorphic complexity*, *Mathematische Zeitschrift* **295** (2020), 1385–1404; first online 22 November 2019. https://doi.org/10.1007/s00209-019-02426-2
