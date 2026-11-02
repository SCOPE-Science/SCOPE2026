# Uniform automaticity of the terminal-three anti-recurrence family

## Finding

**Theorem.** For every integer \(a\ge2\), let \(A_1<A_2<\cdots\) and \(B_1<B_2<\cdots\) be complementary sequences of positive integers satisfying
\[
A_n=aB_{2n-1}+3B_{2n}\qquad(n\ge1).
\]
Put \(\tau=a+3\) and \(\kappa=2\tau+1=2a+7\). Then each interval
\[
I_m=\{\kappa m+1,\ldots,\kappa(m+1)\},\qquad m\ge0,
\]
contains exactly one member \(A_{m+1}=\kappa m+r_m\), where \(4\le r_m\le\kappa\). The offset word \((r_m)_{m\ge0}\) is the fixed point beginning with \(r_0=a+6\) of an explicit \(\tau\)-uniform substitution on at most \(2\tau-2\) letters. In particular, \((A_n-\kappa n)_{n\ge1}\) is \(\tau\)-automatic, proving the Clergyman automaticity assertion for every coefficient vector \((a,3)\) with \(a\ge2\), beyond the published terminal-coefficient-at-most-two theorem. Moreover,
\[
A_{\tau m+1}=\kappa\tau m+a+6\qquad(m\ge0).
\]
The formulas and proof also hold for \(a=1\), which is **already covered** by the previously published individual example; only \(a\ge2\) is claimed as the new family.

The substitution is constructive. With \(S_a=\{4,\ldots,\kappa\}\), for \(r\in S_a\) and \(1\le j\le\tau\), put
\[
T_j(r)=\begin{cases}
\kappa-a-j,&r>2j,\\
\kappa+3-a-j,&r=2j,\\
\kappa+3-j,&r<2j.
\end{cases}
\qquad T(r)=T_1(r)\cdots T_\tau(r).
\]
Then \(T_j(r)\in S_a\) always; \(T(r_0)\) starts with \(r_0\), and the fixed point obeys \(r_{\tau m+j-1}=T_j(r_m)\) for every \(m\ge0\) and \(1\le j\le\tau\).

## Assumptions and scope

All parameters, indices, and sequence elements are **positive integers**, except the block index \(m\ge0\). The complement \(B\) is taken in the positive integers, not in the nonnegative integers. We use the order-two definition of anti-recurrence: each new term is formed from the next two unused complementary numbers. Its elementary greedy construction is uniquely defined, because positive coefficients give \(A_n>B_{2n}\), so the term being inserted cannot be among the complementary terms used to generate it. The theorem covers the whole infinite family with the ordered pair of coefficients \((a,3)\), not arbitrary positive coefficient pairs. Automatic means a **fixed finite automaton** for each fixed parameter \(a\), reading the base-\(\tau\) expansion of the zero-based index and producing the offset as output; it does not assert one automaton works uniformly for unbounded \(a\).

## Proof

**Step 1 (closed transition alphabet).** Fix \(a\ge1\), \(\tau=a+3\), \(\kappa=2\tau+1\), and \(S_a=\{4,\ldots,\kappa\}\). For any \(r\in S_a\), let
\[
1\le c_1<\cdots<c_{2\tau}\le\kappa
\]
be the integers in \(\{1,\ldots,\kappa\}\setminus\{r\}\). Define
\[
T_j(r)=a c_{2j-1}+3c_{2j}-\kappa(j-1),\qquad 1\le j\le\tau.
\]
If \(r>2j\), the two selected complementary positions are \(2j-1,2j\), yielding \(\kappa-a-j\). If \(r=2j\), they are \(2j-1,2j+1\), yielding \(\kappa+3-a-j\). If \(r<2j\), they are \(2j,2j+1\), yielding \(\kappa+3-j\). These are precisely the three stated formulas. In the first case, \(j\le\tau\) gives
\(\kappa-a-j\ge\kappa-a-\tau=4\), and the value is at most \(\kappa\). In the second case, \(r\ge4\) forces \(j\ge2\), so \(\kappa+3-a-j\le\kappa+1-a\le\kappa\) and its value is at least \(\kappa+3-a-\tau=7\). In the third case, \(r\ge4\) forces \(j\ge3\), so \(\kappa+3-j\le\kappa\) and its minimum is \(\kappa+3-\tau=a+7\). Hence \(T_j(S_a)\subseteq S_a\) for every digit \(j\), without exceptions.

**Step 2 (unique self-similar offset word).** Set \(r_0=a+6\in S_a\). Since \(r_0>2\), the first transition gives \(T_1(r_0)=\kappa-a-1=a+6=r_0\). Define \(r_{\tau m+j-1}=T_j(r_m)\) recursively. The only self-reference is the consistent equation at \(m=0,j=1\); every other term uses a strictly smaller index, so the infinite sequence is uniquely defined. The finite alphabet closure of Step 1 holds at every index. Since \(T_1(r)=a+6\) for every \(r\in S_a\), we also have \(r_{\tau m}=a+6\) for every \(m\ge0\).

**Step 3 (complementarity and exact anti-recurrence).** Define
\[
A_{m+1}=\kappa m+r_m\qquad(m\ge0).
\]
Because \(4\le r_m\le\kappa\), the numbers \(A_{m+1}\) are strictly increasing, with exactly one in each disjoint interval \(I_m\). Define \((B_i)_{i\ge1}\) as the increasing enumeration of the complement of the set of all \(A_n\) in the positive integers. Each \(I_m\) has length \(\kappa=2\tau+1\), so it contains exactly \(2\tau\) complementary numbers. With \(c_j\) as in Step 1 at \(r=r_m\), these are exactly
\[
B_{2\tau m+j}=\kappa m+c_j\quad(1\le j\le2\tau).
\]
Consequently, for every \(m\ge0\) and \(1\le j\le\tau\),
\[
\begin{aligned}
aB_{2(\tau m+j)-1}+3B_{2(\tau m+j)}
&=(a+3)\kappa m+a c_{2j-1}+3c_{2j}\\
&=\kappa(\tau m+j-1)+T_j(r_m)\\
&=A_{\tau m+j}.
\end{aligned}
\]
This verifies the defining recurrence for **all** indices. The greedy anti-recurrence is unique by its next-complementary-pair rule, so the constructed pair is exactly the original one. Substituting \(r_{\tau m}=a+6\) gives \(A_{\tau m+1}=\kappa\tau m+a+6\).

**Step 4 (automaticity).** The \(\tau\)-uniform substitution \(r\mapsto T_1(r)\cdots T_\tau(r)\) is prolongable at the initial letter \(r_0\), hence its infinite fixed point is \((r_m)\). Equivalently, a deterministic finite automaton with output has initial state \(r_0\), alphabet of base-\(\tau\) digits \(d\in\{0,\ldots,\tau-1\}\), transition \(\delta(r,d)=T_{d+1}(r)\), and output \(r-\kappa\). The digit-zero transition from the initial state fixes it, so leading zeros cause no ambiguity. The recursion \(r_{\tau m+d}=\delta(r_m,d)\) proves by induction on digit length that the automaton outputs \(r_m-\kappa=A_{m+1}-\kappa(m+1)\). It has at most \(|S_a|=\kappa-3=2\tau-2\) states. This proves the claim.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and no third-party dependencies. Its independent greedy generator follows the next-complementary-pair definition directly, without using the substitution; it is compared to the explicit substitution formula for \(75{,}000\) terms over eight values of \(a\), including parameters as large as \(100\). It also enumerates and checks the substitution's three-branch identity and invariant alphabet for \(5{,}576{,}800\) state-digit cases with \(1\le a\le200\). Expected console message:

\[\texttt{VERIFY\_OK}\]

The finite checks are **not** substituted for any step of the unrestricted proof, which follows from algebraic identities and exact complement counts.

## Relationship to prior work

Fokkink and Joshi, *Anti-Recurrence Sequences* (arXiv:2506.13337; later *Integers* 26 (2026), A24), first publicly posted **2025-06-16**, formulate the Clergyman conjecture that normalized anti-recurrences are automatic. Their Theorem 4 proves this for \(A_1\)-bounded linear forms; for order two this means that the **second coefficient is at most two**. Section 5 exhibits and verifies one single exceptional vector \((1,3)\), which is excluded from the current novelty assertion. The present theorem covers all \((a,3)\) with \(a\ge2\), none of which is \(A_1\)-bounded. It supplies a new invariant offset alphabet \(\{4,\ldots,\kappa\}\), a closed transition rule, and a proof uniform in \(a\). Their specific \((1,3)\) case, known arithmetic-subsequence consequences, and the general definition of anti-recurrence are not claimed as new.

Bosma and collaborators, *Using Walnut to Solve Problems from the OEIS* (arXiv:2503.04122), prove individual anti-bonacci cases with all coefficients one, including three and four complementary terms; these do not imply a variable first coefficient paired with terminal coefficient three. Semantic database searches and direct claim comparisons did not identify a stronger or equivalent published all-\(a\) result. This is a best-knowledge statement, not a certification of priority.

## Limitations

The classification is restricted to two complementary terms and coefficients \((a,3)\). It neither proves the full Clergyman conjecture for arbitrary vectors nor settles the separate \((1,4)\) case noted in the motivating paper. The automaton upper bound \(2\tau-2\) is not claimed minimal. The verification script checks finite parameters and indices, while the proof handles all \(a\ge2\) and every \(n\ge1\). Although primary full texts and database records were inspected, another result in non-indexed or differently named literature might imply this family; historical priority and independent proof review remain open.

## References

1. R. Fokkink and G. Joshi, *Anti-Recurrence Sequences*, arXiv:2506.13337 (first version 2025-06-16); *Integers* 26 (2026), article A24, DOI: 10.5281/zenodo.18305140. Full text: https://math.colgate.edu/~integers/aa24/aa24.pdf.
2. W. Bosma, R. Bruin, R. Fokkink, J. Grube, A. Reuijl, and T. Tromp, *Using Walnut to Solve Problems from the OEIS*, arXiv:2503.04122 (2025); *Journal of Integer Sequences* 28, article 25.3.8 (2025).
3. Mathematical Subject Classification 2020, code 11B85 (automata sequences).
