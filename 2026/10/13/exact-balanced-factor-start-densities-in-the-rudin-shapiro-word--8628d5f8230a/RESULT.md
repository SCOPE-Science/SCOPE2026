# Exact balanced-factor start densities in the Rudin–Shapiro word at lengths \(4^k\)

## Finding
Let \(r_i\in\{0,1\}\) be the parity of the count of overlapping occurrences of the binary digit pair 11 in the binary expansion of \(i\), for \(i\ge0\). For each \(k\ge1\), let \(E_k\) be the set of start indices \(i\) for which the length-\(4^k\) factor of \(r\) has exactly \(4^k/2\) zeros and the same number of ones. Then the natural density exists and is

\[
\lim_{N\to\infty}\frac{|E_k\cap[0,N)|}{N}=\frac{3}{8\cdot 2^k}=\frac{3}{8\sqrt{4^k}}.
\]

The following finite arithmetic classification determines *every* balanced start, not only its density. Consider the fixed point \(u=\mu^\infty(A)\) of the substitution

```
A -> AB
B -> AD
C -> CD
D -> CB
```

under the coding \(A,B\mapsto0\) and \(C,D\mapsto1\). For \(m\ge0\), put \(Q_m=4^m\), \(H_m=2^m\), and

\[
T_m=\left\{1+\sum_{a=0}^{m-1}\varepsilon_a4^a:\varepsilon_a\in\{1,3\}\right\},\quad T_0=\{1\}.
\]

Write \(i=4^k n+j\) with \(0\le j<4^k\). Then \(i\in E_k\) if and only if one of the following *disjoint* cases holds:

1. \(u_nu_{n+1}\in\{AD,BC,CB,DA\}\) and \(j\in T_{k-1}\).
2. \(u_nu_{n+1}\in\{AB,CD\}\) and \(j\in 2\cdot4^{k-1}+T_{k-1}\).

For \(u_nu_{n+1}\in\{BA,DC\}\), there are no balanced starting offsets.

## Assumptions and scope
The word is the one-sided *standard* Rudin–Shapiro sequence indexed from \(0\), with **overlapping** 11-pairs counted. The natural density counts start indices, not distinct word factors. Every assertion holds for all integer \(k\ge1\), with no finite cutoff. A factor is called balanced here solely if it has equal letter multiplicities; there is no assumption that the entire infinite word is balanced in the bounded-discrepancy sense.

The coding of \(u\) gives \(r\): even positions of \(u\) are in \(\{A,C\}\), odd positions in \(\{B,D\}\). Writing \(a(i)=(-1)^{r_i}\), the substitution implies \(a(0)=1\), \(a(2n)=a(n)\), and \(a(2n+1)=(-1)^na(n)\). These are the classical Rudin–Shapiro recurrences and uniquely determine the sequence.

## Proof
**Block prefix lemma.** For \(m\ge0\), let \(W_{X,m}=\mu^{2m}(X)\), of length \(Q_m\), and let \(P_{X,m}(j)\) be the sum of its first \(j\) coded signs, taking \(A,B\) to \(+1\) and \(C,D\) to \(-1\). Write \(H=H_m\), \(Q=Q_m\). For \(X=A,B\), the full-block sum is \(H\), and for all \(1\le j\le Q\),

\[
0<P_{A,m}(j)\le2H-1,\qquad0<P_{B,m}(j)\le H.
\]

Moreover \(P_{A,m}(j)=H\) exactly at the same offsets as \(P_{B,m}(j)=H\), namely at \(j\in T_m\). These facts hold at \(m=0\): both blocks have one positive sign and \(T_0=\{1\}\). In general, the substitution commutes with the letter involution \(A\leftrightarrow C\), \(B\leftrightarrow D\), so \(P_{C,m}=-P_{A,m}\) and \(P_{D,m}=-P_{B,m}\). The two-level iterates satisfy

\[
W_{A,m+1}=W_{A,m}W_{B,m}W_{A,m}W_{D,m},\qquad
W_{B,m+1}=W_{A,m}W_{B,m}W_{C,m}W_{B,m}.
\]

Their four consecutive \(Q\)-blocks have cumulative initial sums \(0,H,2H,3H\) and \(0,H,2H,H\), respectively; the final total in each is \(2H\). The strict prefix inequalities and upper bounds follow blockwise from the induction hypotheses. In both concatenations, the value \(2H\) is reached only in the second block at the previous offsets \(T_m\), or in the fourth block at those same offsets. On the second block it occurs at \(Q+T_m\), and on the fourth at \(3Q+T_m\). The possible boundary equality at the entry of the third block is already counted in \(Q+T_m\) because \(Q\in T_m\). Thus

\[
T_{m+1}=(Q_m+T_m)\,\dot\cup\,(3Q_m+T_m),
\]

and hence the claimed base-four digit description and \(|T_m|=2^m\), completing the induction.

**Balanced-window lemma.** Let \(m=k-1\), so \(4^k=4Q\) and the sum of a positive \(W_{A,m+1}\) or \(W_{B,m+1}\) block is \(2H\). Every window of length \(4Q\) starting at \(i=4Qn+j\) comprises the suffix of \(W_{u_n,m+1}\) after \(j\) signs and the prefix of \(W_{u_{n+1},m+1}\) through \(j\) signs. Its signed sum is

\[
S_{u_n}-P_{u_n,m+1}(j)+P_{u_{n+1},m+1}(j),
\]

with \(S_A=S_B=2H\), \(S_C=S_D=-2H\). Balance is equivalent to \(P_X(j)-P_Y(j)=S_X\). The only adjacent state pairs in \(u\) are \(AB,AD,BA,BC,CB,CD,DA,DC\). For \(AD\) and \(BC\), the four blocks for the two letters agree in the last two positions and have opposite signs in the first two. Their prefix difference equals \(2P_{A,m}(j)\) for \(0\le j\le Q\), then \(2H+2P_{B,m}(j-Q)\) for \(Q\le j\le2Q\), then \(4H\). The equation with right-hand side \(2H\) therefore holds exactly for \(j\in T_m\). Complementarity gives the same conclusion for \(CB\) and \(DA\).

For \(AB\), the initial two \(Q\)-blocks agree, the third differs by opposite signs \(A/C\), and the fourth by \(D/B\). Thus the prefix difference is zero through \(2Q\), then \(2P_{A,m}(j-2Q)\) for \(2Q\le j\le3Q\), then \(2H-2P_{B,m}(j-3Q)\). Equality to \(2H\) occurs precisely for \(j\in2Q+T_m\); complementarity handles \(CD\). Reversing \(AB\) and \(CD\) negates the respective difference, ruling out balance for \(BA\) and \(DC\). This proves the exact classification.

**Density.** The substitution is primitive (each third iterate contains every letter), so all letter and adjacent-pair frequencies exist. The letter frequencies are \(1/4\) each: the normalized incidence matrix has uniform stationary vector, which is unique by primitivity. The internal pairs \(AB,AD,CD,CB\) each occur once per image of their corresponding letter, so have limiting frequency \(1/8\). All remaining allowed pairs are boundary pairs. Their frequencies satisfy

\[
2p_{BA}=p_{AB}+p_{DA},\quad 2p_{DA}=p_{BA}+p_{CB},
\]
\[
2p_{BC}=p_{AD}+p_{DC},\quad 2p_{DC}=p_{BC}+p_{CD}.
\]

Consequently all eight adjacent-pair frequencies are \(1/8\). Among the \(4^k\) offsets for each fixed pair, exactly six pair types admit \(|T_{k-1}|=2^{k-1}\) balanced starts and two admit none. Passing from adjacent-letter frequencies to starts at all indices multiplies by \(1/4^k\) because there are \(4^k\) disjoint start-offset classes in each superblock. Therefore

\[
\operatorname{dens}(E_k)=\frac{6}{8}\frac{2^{k-1}}{4^k}=
\frac{3}{8\cdot2^k}.
\]

## Verification
Run \(`python3 verify.py`\). The standalone verifier independently generates 131072 Rudin–Shapiro signs by counting overlapping 11 digit-pairs and compares them pointwise with the substitution coding. It checks the prefix and zero-level induction assertions for seven successive scales and checks **every** balanced-window start at lengths \(4,16,64,256,1024,4096\) in that finite word against the base-four classification. These are finite cross-checks of the explicit induction; they are not used as an infinite proof.

## Relationship to prior work
Mol, Rampersad and Shallit (2023; arXiv:2301.06145) investigate Dyck factors of the Rudin–Shapiro and other automatic words, including existence and nesting questions; their Rudin–Shapiro results concern Dyck-factor existence and lengths, not the natural density of *all zero-sum factor starts* at fourth-power lengths. Rampersad and Shallit (2023; arXiv:2302.00405) study the global Rudin–Shapiro summatory functions, synchronized representations, extrema, and level-set counts; those results do not state the local fixed-window density or the base-four offset classification. The present statement is not a count of distinct factors, nor a consequence of an arbitrary global prefix-sum bound. Searches for equivalent formulations and stronger coverings did not locate the precise statement; priority uncertainty remains.

## Limitations
The formula is asserted only at lengths \(4^k\), \(k\ge1\), for this one standard binary automatic word. No formula is claimed for other lengths, other automatic words, or for Dyck-factor (nonnegative-prefix) frequencies. Earlier stronger results on Rudin–Shapiro summatory functions could conceal an equivalent implicit deduction; no exhaustive literature-unicity claim is made.

## References
1. L. Mol, N. Rampersad, J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145, first public January 15, 2023, https://arxiv.org/abs/2301.06145.
2. N. Rampersad, J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, arXiv:2302.00405, first public February 1, 2023, https://arxiv.org/abs/2302.00405; Theory of Computing Systems (2025), DOI:10.1007/s00224-025-10214-1.
