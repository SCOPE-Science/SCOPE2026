# Run-limited binary words: exact subsequence-universality spectrum and sharp forcing thresholds

## Finding
Fix an integer \(R\ge1\). For every length \(n\ge0\) and every \(k\ge0\), let \(N_R(n,k)\) count indexed binary words in which each maximal constant-symbol run has length at most \(R\) and whose scattered-subsequence universality index is exactly \(k\). Define
\[
A_R(z)=\sum_{j=0}^{R-1}z^j,\qquad A_0(z)=0,\qquad T_R(z)=A_R(z)+A_{R-1}(z).
\]
The complete, simultaneous length-and-index distribution is
\[
\boxed{\sum_{n,k\ge0}N_R(n,k)z^nu^k
 =1+\frac{2z A_R(z)(1+uz)}{1-uz^2T_R(z)}.}
\]
In particular, for every \(k\ge1\),
\[
\sum_{n\ge0}N_R(n,k)z^n
=2z^{2k}A_R(z)\,T_R(z)^{k-1}\bigl(1+zT_R(z)\bigr).
\]
The constant-index terms are \(N_R(0,0)=1\) and \(N_R(n,0)=2\) precisely for \(1\le n\le R\). For each \(k\ge0\), the nonzero length range for index \(k\) is \(2k\le n\le (R+1)k+R\), with the empty-word convention at \(k=0\). Every integer in this interval occurs, and the upper-end coefficient is exactly \(2\). For each \(k\ge1\), **every** allowed length-\((R+1)k\) word is \(k\)-universal, and exactly two allowed length-\(((R+1)k-1)\) words fail to be \(k\)-universal. Thus the worst-case threshold is sharp for all \(R,k\). Explicit upper-end witnesses are \(0^R(10^R)^k\) and its complement.

## Assumptions and scope
A word of length \(n\) is an indexed finite string over the fixed alphabet \(\{0,1\}\); different positions matter even if words are rotations. A scattered subsequence preserves order but may skip positions. The index \(\iota(w)\) is the largest integer \(k\) such that **every** binary length-\(k\) target occurs as a scattered subsequence of \(w\). The empty word has index zero, as does a nonempty one-symbol-only word. Runs are maximal contiguous segments of equal symbols, including a run at either endpoint. The constraint applies to *both* symbols, not just one. All displayed identities are formal power-series identities over integer coefficients; no convergence assumptions are required.

## Proof
**Arch decomposition.** Scan a binary word from left to right, closing a complete *arch* whenever the second distinct symbol since the beginning of that arch first appears, and restarting immediately after that closing position. Each complete binary arch ends in a symbol different from its initial symbol. The standard greedy-arch characterization says that the number of complete arches is exactly \(\iota(w)\). In brief, choosing one occurrence of each target symbol in consecutive complete arches proves universality at the number of arches; the incomplete remainder supplies a binary symbol absent from its own final segment, and recursively selecting absent symbols produces a length-one-longer target that cannot be embedded. This greedy fact is also proved in the cited arch-factorization literature.

**Run-bounded continuation automaton.** Let \(E\) be the bivariate generating series for all permissible continuations after a complete arch. The most recent symbol, which closed that arch, has run length one, and the current (new) arch is empty. Let \(S_j\) be the generating series for continuations in an incomplete arch containing only one distinct symbol, where the last constant run has length \(j\), for \(1\le j\le R\). Continuations include the option to stop immediately, with weight one. The next symbol in state \(S_j\) either equals the current symbol (permitted only for \(j<R\), giving the state \(S_{j+1}\)) or differs from it (thereby closing one arch, contributing a factor \(u\), and entering \(E\)); each appended symbol contributes \(z\). Consequently
\[
S_R=1+uzE,\qquad S_j=1+zS_{j+1}+uzE\quad(1\le j<R).
\]
Iterating yields \(S_1=A_R(z)(1+uzE)\) and, for \(R\ge2\), \(S_2=A_{R-1}(z)(1+uzE)\). When \(R=1\), the second state is unavailable, which is encoded by \(A_0(z)=0\). At \(E\), the next bit is either the complement of the previous bit (enter \(S_1\)) or the same bit if the run bound permits it (enter \(S_2\)); hence
\[
E=1+z\bigl(S_1+S_2\bigr)=1+zT_R(z)(1+uzE).
\]
Solving formally gives \(1+uzE=(1+uz)/(1-uz^2T_R(z))\). The first symbol of any nonempty word admits two choices and leaves state \(S_1\), so the required series is \(1+2zS_1\). This proves the asserted rational identity for all \(R\).

**Exact length range and forcing.** Expand the denominator as \(\sum_{j\ge0}u^jz^{2j}T_R(z)^j\). For \(k\ge1\), the two ways to obtain \(u^k\) (with or without using the numerator's \(uz\)) produce precisely the coefficient polynomial in the statement. The polynomial \(A_R\) has a positive coefficient at every degree from zero through \(R-1\); likewise \(T_R\) has positive coefficients through \(R-1\) (for \(R=1\), both polynomials equal one). Therefore all powers have no internal gaps, and the support is exactly \([2k,(R+1)k+R]\). The unique leading-degree choices in \(A_R\), each \(T_R\), and the final \(zT_R\) each have coefficient one, so the leading coefficient is two. This establishes the maximal length and extremal count. Since index at most \(k-1\) forces length at most \((R+1)(k-1)+R=(R+1)k-1\), every permissible word at length \((R+1)k\) is \(k\)-universal. At length \((R+1)k-1\), the just-proved leading coefficient for index \(k-1\) equals two; these are precisely the two failures. The two extremizers can be read directly as \(0^R(10^R)^k\) and its bit complement, completing the sharpness proof.

## Verification
The standalone program `verification/verify.py` computes the displayed polynomial coefficients without using greedy state transitions, and separately computes the index by checking each binary subsequence target. It exhaustively checks every run-limited word at lengths zero through twelve for \(1\le R\le6\), totaling 26,598 test words. A third implementation, using a direct four-component dynamic-programming state machine, checks 57,036 length/index cells for \(1\le R\le12\) and lengths through 96. Extremal supports, exact endpoint multiplicities, and explicit witness indices were additionally checked for \(k\le14\). Output: `RLL_BINARY_UNIVERSALITY_PASS`. Computations test finite instances; the preceding argument proves all parameter values.

## Relationship to prior work
Barker et al. (2020) and Fleischmann et al. (2021) develop greedy-arch characterizations for subsequence universality, on which the first proof step relies. Kovačević and Vukobratović (2021) analyze runlength-limited sequence enumeration by run and weight statistics. Their statistics cannot by themselves determine the universality index: for example the two run-bounded words `0010011` and `0011001` have equal length, weight, and number of runs but respectively have universality indices \(2\) and \(3\). An unrestricted binary length/index generating function does not by itself determine the joint distribution after restricting both run types to lengths at most \(R\). The present theorem gives this joint distribution and its sharp forcing boundary simultaneously for every allowed \(R\).

## Limitations
The alphabet here is binary, the run cap applies to both symbols, the index concerns *scattered* subsequences rather than contiguous factors, and words are counted with their positions distinguished rather than modulo reversal/rotation. This theorem does not enumerate distinct subsequence sets, constrained-gap embeddings, or nonbinary universality indices. Computational verification is finite and is not a substitute for the mathematical proof. A different-language derivation of the same distribution may exist in literature not inspected here.

## References
Barker, Fleischmann, Harwardt, Manea, and Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (first public 2020-03-10).

Fleischmann, Germann, and Nowotka, *Scattered Factor Universality — The Power of the Remainder*, arXiv:2104.09063 (2021-04-19).

Kovačević and Vukobratović, *Asymptotic Behavior and Typicality Properties of Runlength-Limited Sequences*, arXiv:2105.04617 (2021-05-10).
