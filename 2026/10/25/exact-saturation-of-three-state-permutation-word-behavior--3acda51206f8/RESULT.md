# Exact saturation of three-state permutation-word behavior

## Finding

For every integer \(n\ge1\), partition binary words \(w\in\{0,1\}^{n}\) by their behavior under **all** assignments of the two letters to permutations of three states: \(u\sim_3v\) if \(u(\sigma_0,\sigma_1)=v(\sigma_0,\sigma_1)\) for every \(\sigma_0,\sigma_1\in S_3\). Let \(N_3(n)\) count the classes. The exact finite-length profile is

\[
\begin{array}{c|rrrrrrrrrrrrr}
n&1&2&3&4&5&6&7&8&9&10&11&12&13\\\hline
N_3(n)&2&4&8&15&26&41&60&84&108&133&148&159&162.
\end{array}
\]

Moreover, \(N_3(n)=162\) for every \(n\ge13\). Thus **thirteen is the least common length at which every one of the 162 possible three-state permutation behaviors of a binary word is represented**. Equivalently, the same classes are the indistinguishability classes of binary words under three-state permutation automata, permitting arbitrary initial and final state choices.

## Assumptions and scope

Words are **positive**, with no inverse letters, and have a common fixed length \(n\). A word acts through composition of its letter permutations, with two words equivalent when their resulting transformations agree for all \(36\) ordered assignments of the two letters in \(S_3\). This is not equivalence under arbitrary (possibly nonpermutation) three-state automata, nor does the result claim a new asymptotic word-separation lower bound.

Let \(z(w)\) be the number of zeros modulo \(6\). Number positions from \(0\) and define, with each sum interpreted modulo \(3\),

\[
\begin{aligned}
A(w)&=\sum_{j:w_j=1}(-1)^{\#\{i<j:w_i=0\}},\\
B(w)&=\sum_{j:w_j=0}(-1)^{\#\{i<j:w_i=1\}},\\
C(w)&=\sum_{j:w_j=0}(-1)^j.
\end{aligned}
\]

Write \(\Phi(w)=(z(w),A(w),B(w),C(w))\in \mathbb Z/6\mathbb Z\times(\mathbb Z/3\mathbb Z)^3\). The theorem includes the exact characterization

\[
u\sim_3v\quad\Longleftrightarrow\quad\Phi(u)=\Phi(v)\qquad(u,v\in\{0,1\}^n).
\]

## Proof

**1. A complete signature.** Identify \(S_3\) with \((\mathbb Z/3\mathbb Z)\rtimes(\mathbb Z/2\mathbb Z)\) under \((r,e)(s,f)=(r+(-1)^e s,e+f)\). Write the assigned images of the two letters as \((r,e)\) and \((s,f)\). If \(h(m)=\sum_{j=0}^{m-1}(-1)^j\), the translation coordinate of the evaluated word is as follows:

\[
\begin{array}{c|c}
(e,f)&\text{translation modulo }3\\\hline
(0,0)&r\,z+s\,(n-z)\\
(1,0)&r\,h(z)+s\,A\\
(0,1)&r\,B+s\,h(n-z)\\
(1,1)&r\,C+s\,[h(n)-C].
\end{array}
\]

The parity coordinate is \(e z+f(n-z)\) modulo \(2\). In these formulas \(z\) is any integral representative of the number of zeros; all relevant expressions depend only on its residue modulo \(6\). Consequently, \(\Phi(u)=\Phi(v)\) forces equality for all permutation assignments. Conversely, assignments with \((e,f)=(0,0)\) and \(r=1,s=0\) recover the zero count modulo \(3\); an assignment with \(e=1,f=0\) recovers its parity. The three assignments with \((e,f;r,s)=(1,0;0,1)\), \((0,1;1,0)\), and \((1,1;1,0)\) recover respectively \(A,B,C\). Thus all four signature components are necessary. There are at most \(6\cdot3^3=162\) signatures.

**2. Finite recurrence and exact counts.** A signature \((z,a,b,c)\) of a length-\(n\) word has the following successors after appending a letter:

\[
\begin{aligned}
0:&\quad ((z+1)\bmod6,\ a,\ b+(-1)^{n-z},\ c+(-1)^n),\\
1:&\quad (z,\ a+(-1)^z,\ b,\ c),
\end{aligned}
\]

where the last three coordinates are reduced modulo \(3\). The exponents use only integer parity, so any representative of \(z\) modulo \(6\) is legitimate. Starting from the singleton \(\{(0,0,0,0)\}\) at length zero and replacing each reachable set by the union of both types of successors gives exactly the displayed counts at lengths \(1\) through \(13\). At each of lengths \(13,14,15,16,17,18\) the reachable set equals the entire 162-element signature space. The included standalone verifier gives an exhaustive finite check of precisely this recurrence, including an independent direct 36-assignment permutation evaluation at lengths at most eight.

**3. Infinite-length conclusion.** Every permutation in \(S_3\) has order dividing \(6\). For words of equal length, the map \(w\mapsto w0^6\) preserves all evaluated permutations and cannot identify distinct behavior classes. Therefore \(N_3(n+6)\ge N_3(n)\) for every \(n\). Each \(n\ge13\) is congruent modulo \(6\) to one of the six base lengths \(13\) through \(18\). Since all six already realize 162 signatures and no length can realize more, \(N_3(n)=162\) for all \(n\ge13\). Every earlier length has fewer than 162 classes by the finite table, establishing sharpness.

## Verification

Run \(\texttt{python3 verify\_s3\_behavior.py}\) using Python's standard library. The program independently derives the signature of individual words, propagates all reachable signatures through length 18, and compares its partition against direct evaluations of all 36 pairs of three-point permutations for every binary word of length at most eight. It asserts the displayed finite counts and the full 162-element set at all six base lengths and reports \(\texttt{VERIFY\_OK}\). This finite computation establishes only the bounded recurrence certificate; the separate period-six argument supplies the assertion for all lengths.

## Relationship to prior work

Xu and Regan (2026) study asymptotic word separation by permutation automata and relate it to positive binary identities of symmetric groups. Bulatov, Karpova, Shur, and Startsev (2017), Section 3, record the classical shortest positive identity \(x^2y^2=y^2x^2\) in \(S_3\). Kearnes (2018) computed the two-generator relatively free group in the variety of \(S_3\) to have order \(972\). That **already settles the total number of coefficient-free group term functions**, and is not claimed as new here. The separate result here is the fixed-length positive-word realization profile and its sharp common-length saturation threshold \(13\). The cited 2021 investigation of positive identities primarily reports short identities in larger symmetric groups; only its abstract was accessible for inspection.

## Limitations

The result is specific to binary words and three-state *permutation* actions. The recurrence certificate is finite and elementary, not an asymptotic complexity analysis. The positive-word saturation threshold need not characterize the minimal-length representatives when inverse letters are allowed, or automata with arbitrary transitions. While the checked primary literature and research records did not report this exact length profile, related earlier finite-group word-growth literature and the unavailable full text of Karpova--Shur (2021) create residual originality risk. No independent mathematical audit has been performed.

## References

1. C. Xu and K. Regan, *An Improved Lower Bound for Separating Words by Permutation Automata*, arXiv:2610.11098, first public version 8 October 2026. https://arxiv.org/abs/2610.11098
2. A. Bulatov, O. Karpova, A. Shur, K. Startsev, *Lower Bounds on Words Separation: Are There Short Identities in Transformation Semigroups?*, Electronic Journal of Combinatorics 24(3) (2017), P3.35, Section 3. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p35/pdf/
3. K. Kearnes, answer to *Relatively free groups in Var(S3)*, MathOverflow, 16 September 2018 (group order 972). https://mathoverflow.net/questions/153883/relatively-free-groups-in-vars-3/154009
4. O. Karpova and A. Shur, *Words Separation and Positive Identities in Symmetric Groups*, Journal of Automata, Languages and Combinatorics 26(1-2) (2021), 67–89 (abstract consulted). https://jalc.de/issues/2021/issue_26_1-2/abs-067.pdf
