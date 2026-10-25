# Sharp length-thirteen saturation of three-state permutation-word equivalence

## Finding

Let \(\Sigma=\{0,1\}\). Two words \(u,v\in\Sigma^n\) are *three-state permutation-equivalent* if, for every pair of permutations \(\sigma_0,\sigma_1\in S_3\), their evaluated permutations agree. Equivalently, no permutation deterministic automaton with at most three states can distinguish them. Write \(E(n)\) for the number of equivalence classes in \(\Sigma^n\).

**Theorem.** The exact length profile is
\[
(E(0),E(1),\ldots,E(12))=(1,2,4,8,15,26,41,60,84,108,133,148,159),
\]
whereas
\[
\boxed{E(n)=162\quad\text{for every integer }n\ge13.}
\]
The threshold is sharp: \(E(12)=159<162\). Moreover, equality of two same-length words is decided by the four residues defined below, and every admissible residue quadruple occurs already at length thirteen.

## Assumptions and scope

Words are finite, ordered, and binary; the empty word is included only at length zero. Automaton letters act as permutations of three states, not arbitrary state transformations. The equivalence tests *all* choices of both letter permutations and *all* starting states. Every one- or two-state permutation automaton embeds by fixed states into a three-state automaton.

For a word \(w=w_1\cdots w_n\), write \(N_0(w)\) and \(N_1(w)\) for its symbol counts and set
\[
\begin{aligned}
R(w)&=N_0(w)\pmod6,\\
T(w)&=\sum_{j:w_j=0}(-1)^{\#\{i<j:w_i=1\}}\pmod3,\\
U(w)&=\sum_{j:w_j=1}(-1)^{\#\{i<j:w_i=0\}}\pmod3,\\
V(w)&=\sum_{j:w_j=0}(-1)^{j-1}\pmod3.
\end{aligned}
\]
Choose each residue representative from \(\{0,1,\ldots,5\}\) for \(R\) and \(\{0,1,2\}\) for the other three. The theorem's equivalence criterion is
\[
u\sim_n v\quad\Longleftrightarrow\quad
(R(u),T(u),U(u),V(u))=(R(v),T(v),U(v),V(v)).
\]
These four word invariants are denoted \( (r,T,U,V)\) when they are treated as elements of the finite signature state space.

## Proof

**1. Affine normal form and a complete signature.** Every permutation of three points is uniquely an affine map \(z\mapsto\varepsilon z+a\) on \(\mathbb F_3\), with \(a\in\mathbb F_3\) and \(\varepsilon\in\{+1,-1\}\). Use the group convention in which a word's letters are multiplied left to right as affine maps. For a fixed assignment of the two letter signs \((\varepsilon_0,\varepsilon_1)\), the product for \(w\) has sign \(\varepsilon_0^{N_0(w)}\varepsilon_1^{N_1(w)}\) and translation
\[
A_w(\varepsilon_0,\varepsilon_1)a_0+B_w(\varepsilon_0,\varepsilon_1)a_1,
\]
where
\[
A_w=\sum_{j:w_j=0}\prod_{i<j}\varepsilon_{w_i},\qquad
B_w=\sum_{j:w_j=1}\prod_{i<j}\varepsilon_{w_i}\pmod3.
\]
The opposite convention for reading automata yields the same identities: invert each substituted letter permutation and invert the resulting product, a bijection on substitutions.

For the four possible sign choices, direct alternating-sum identities give
\[
\begin{array}{c|cc}
(\varepsilon_0,\varepsilon_1)&A_w&B_w\\\hline
(+,+)&N_0(w)&N_1(w)\\
(-,+)&N_0(w)\bmod2&U(w)\\
(+,-)&T(w)&N_1(w)\bmod2\\
(-,-)&V(w)&(n\bmod2)-V(w)
\end{array}\quad\text{in }\mathbb F_3.
\]
The length \(n\) and \(r=R(w)=N_0(w)\bmod6\) determine all the fixed entries and the total signs. Conversely, varying the two translation parameters \(a_0,a_1\) independently shows that equality of evaluated permutations for every assignment requires equality of all coefficients; these recover \(r,T,U,V\). Hence the four-residue criterion is exact. There are at most \(6\cdot3^3=162\) classes at each length.

**2. Exact finite reachability.** Let \(R_n\subseteq\mathbb Z/6\mathbb Z\times(\mathbb F_3)^3\) be the reachable signatures at length \(n\). The initial set is \(R_0=\{(0,0,0,0)\}\). Appending a zero or one gives, respectively,
\[
\begin{aligned}
F_{n,0}(r,T,U,V)&=(r+1,\;T+(-1)^{n-r},\;U,\;V+(-1)^n),\\
F_{n,1}(r,T,U,V)&=(r,\;T,\;U+(-1)^r,\;V),
\end{aligned}
\]
with the first coordinate reduced modulo six and others modulo three. Therefore
\[
R_{n+1}=F_{n,0}(R_n)\cup F_{n,1}(R_n).
\]
This is a finite exact recurrence on 162 states, not a statistical experiment. Iterating it for \(n\le13\) gives the displayed profile and \(|R_{13}|=162\); the bundled `CERTIFICATE.tsv` provides one explicit thirteen-symbol representative for each of the 162 signatures. The bundled `verify.py` reconstructs all \(R_n\) for \(0\le n\le13\), replays every certificate row, and independently evaluates every binary word through length thirteen in all 36 pairs of permutations of three symbols. Both methods agree.

**3. Infinite stabilization.** For each fixed \(n\), both maps \(F_{n,0}\) and \(F_{n,1}\) are bijections on the entire 162-element signature space: in each case the changed coordinates are affine translations, and the zero transition also shifts \(r\) by one. Since \(R_{13}\) is the full space, \(R_{14}\) contains \(F_{13,0}(R_{13})\), which is again full. Induction gives \(R_n\) equal to the full space for every \(n\ge13\). The strict inequality at twelve establishes the sharp threshold. \(\square\)

## Verification

Using Python 3 with no third-party dependencies, run `python verify.py` in the directory containing `CERTIFICATE.tsv`. The checker asserts the exact fourteen-entry prefix \((E(0),\ldots,E(13))\), explicitly enumerates all 162 possible signatures at level thirteen, validates all 162 witness words and independently compares the compressed signature with direct evaluation in \(S_3\) for all \(\sum_{j=0}^{13}2^j\) binary words. It also checks both letter transitions are permutations of the full signature universe. The infinite assertion uses the proven bijective transition argument; it is not an extrapolation of the finite census.

## Relationship to prior work

Permutation-word separation and positive identities in symmetric groups were studied by Bulatov, Karpova, Shur, and Startsev (2017), who record the shortest positive identity in \(S_3\) but do not enumerate equivalence classes by length. Xu and Regan (2026) improve asymptotic separation lower bounds through short positive identities for large symmetric groups; they define the identity/separation correspondence but do not give the present length-resolved three-state quotient or its sharp saturation index. Karpova and Shur (2021) treat positive identities, especially for \(S_5\) and \(S_6\); only the accessible abstract was examined in this round, so full-text overlap there remains a residual risk. The affine representation of \(S_3\) is classical; the novelty assessed here is the complete exact length profile and sharp realization threshold, not the group representation itself.

## Limitations

This theorem concerns a fixed three-state permutation bound and binary equal-length words. It does not address nonpermutation automata, larger permutation groups, or the asymptotics of state requirements. The sharp profile is the result of finite exact symbolic reachability combined with a proof of stabilization; independently published equivalent classifications may exist outside the examined sources. Independent scientific audit has not been performed.

## References

- C. Xu and K. Regan, *An Improved Lower Bound for Separating Words by Permutation Automata*, arXiv:2610.11098v1, first publicly posted 2026-10-08; https://arxiv.org/html/2610.11098v1.
- A. A. Bulatov, O. Karpova, A. M. Shur, and K. Startsev, *Lower Bounds on Words Separation: Are There Short Identities in Transformation Semigroups?*, Electronic Journal of Combinatorics 24(3), P3.35 (2017), DOI:10.37236/6450.
- O. Karpova and A. M. Shur, *Words Separation and Positive Identities in Symmetric Groups*, Journal of Automata, Languages and Combinatorics 26(1–2), 67–89 (2021), DOI:10.25596/jalc-2021-067 (abstract available; full text not examined here).
