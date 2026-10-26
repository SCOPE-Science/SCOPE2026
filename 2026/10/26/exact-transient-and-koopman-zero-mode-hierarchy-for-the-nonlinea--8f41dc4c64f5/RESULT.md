# Exact transient and Koopman zero-mode hierarchy for the nonlinear rule-154 cellular automaton

## Finding

For the elementary binary cellular automaton of Wolfram rule 154 on a periodic ring of size \(N=2m\ge4\), put \(q=2^{\nu_2(m)}\). The exact number of configurations in the image of the \(t\)-th iterate is, for every integer \(t\ge0\),
\[
 |F^t(\{0,1\}^{2m})|=2^{2m}-2^{m+1}+2^{m-\min(t,q)+1}.
\]
All configurations eventually lie on cycles by time \(q\), and this threshold is attained. Precisely \(2^{m-q+t}\) states enter their eventual cycle for the first time at step \(t\), for every \(1\le t\le q\), with none having greater preperiod.

The Koopman operator \(K\) on complex functions on the \(2^{2m}\) configurations, \((K\phi)(x)=\phi(F(x))\), has algebraic zero-eigenvalue multiplicity
\[
 M_0=2^{m+1}-2^{m-q+1},
\]
with exactly \(2^{m-t}\) Jordan blocks of size \(t\) for each \(1\le t<q\), and \(2^{m-q+1}\) blocks of size \(q\). When \(q=1\), only the last clause applies and there are \(2^m\) blocks of size one. The zero-eigenvalue *fraction* of the full Koopman matrix is therefore
\[
 2^{1-m}(1-2^{-q}).
\]
For odd ring length \(N\ge3\), the cellular automaton is bijective and the Koopman operator is unitary.

## Assumptions and scope

Indices are taken modulo \(N\). Binary operations take place in \(\mathbb F_2\). Define
\[
 F(x)_i=x_{i-1}+x_{i+1}+x_i x_{i+1}\pmod2.
\]
The truth table is rule 154 in the conventional Wolfram ordering. The **preperiod** of a finite-state configuration is the smallest \(t\ge0\) for which its image after \(t\) updates belongs to a periodic orbit. A Jordan block size refers to the algebraic generalized eigenspace of eigenvalue zero, over \(\mathbb C\). All formulas above hold for every permitted \(N\), not solely the checked finite sizes. No statement is made about the other eigenvalues' individual multiplicities, although those eigenvalues are roots of unity.

## Proof

**1. A collision graph with no odd cycles.** The local rule \(f(a,b,c)=a+c+bc\) is left-permutive. If two cyclic configurations of equal output agree at a consecutive symbol pair, then the local equation propagates their agreement one position backward around the ring, so they are identical. Thus any distinct pair of preimages of one output follows a directed cycle through the twelve *off-diagonal* pair states \((a,b,A,B)\) with \((a,b)\ne(A,B)\). The edge condition from \((a,b,A,B)\) to \((b,c,B,C)\) is \(f(a,b,c)=f(A,B,C)\). Writing each state as four binary digits, the complete off-diagonal edge table is

```
0001: 0010,0011
0010: 0001,0100
0011: 0110,0111
0100: 1000,1100
0110: 1001,1101
0111: (none)
1000: 0001,0100
1001: 0110,0111
1011: 0010,0011
1100: 1001,1101
1101: (none)
1110: 1000,1100
```

The only recurrent strongly connected components are \(\{0001,0010,0100,1000\}\) and \(\{0110,1001\}\). Both recurrent components are bipartite, so every directed cycle has even length. This proves injectivity, hence bijectivity, at odd \(N\). For even \(N\), a collision cycle in either component has each input's ones confined to one alternating parity class: the first component consists of mutually exclusive alternating supports, and the second of opposite alternating supports. In particular, every collision consists of configurations that are supported on a single parity class.

**2. Invariant exceptional sector.** On a ring of size \(2m\), let \(U\) be the union of configurations supported on the even sites and configurations supported on the odd sites, including the all-zero configuration once. Then \(|U|=2^{m+1}-1\). Direct substitution into the rule shows \(F(U)\subset U\): on either parity sector the output belongs to the opposite one. If \(y=F(x)\) vanishes at every odd site, write \(a_j=x_{2j}\), \(b_j=x_{2j+1}\). The zero-output equations give
\[
 a_j=(1+b_j)a_{j+1}\quad(j\bmod m).
\]
If some \(b_j=1\), cyclic propagation forces every \(a_j=0\); if every \(b_j=0\), \(x\) already belongs to the even sector. Interchanging the two parity classes establishes \(F^{-1}(U)=U\). Hence the complement \(O=\{0,1\}^{2m}\setminus U\) is forward invariant. By the collision-graph lemma, \(F\) is injective on \(O\), and finiteness makes \(F|_O\) a permutation. Its cardinality is \(2^{2m}-2^{m+1}+1\).

**3. Linear dynamics within the exceptional sector.** Identify each parity sector with \(\mathbb F_2^m\), and let \(S\) be cyclic translation of \(m\) coordinates. At each update, a vector supported on one parity goes to the other parity after multiplication by \(I+S\) or \(I+S^{-1}\). Since \(I+S^{-1}=S^{-1}(I+S)\), after \(t\) steps, the linear operator is a coordinate shift times \((I+S)^t\). Write \(m=qu\), with \(u\) odd and \(q\) a power of two. In \(\mathbb F_2[z]\),
\[
 z^m-1=(z^u-1)^q=(z+1)^q Q(z),\qquad Q(1)\ne0.
\]
The cyclic representation \(\mathbb F_2[z]/(z^m-1)\) splits into a \(q\)-dimensional primary factor for \(z+1\), where multiplication by \(1+z\) is nilpotent of index \(q\), and an \((m-q)\)-dimensional factor where it is invertible. Consequently
\[
 \operatorname{rank}(I+S)^t=m-\min(t,q).
\]
The images of the two parity sectors overlap only in the zero state, so the image of their union after \(t\) updates has \(2^{m-\min(t,q)+1}-1\) states. Add the invariant permutation sector \(O\) to obtain the exact image-size formula above. After time \(q\), both restricted linear maps are permutations on their stabilized images; the whole image is therefore periodic. For \(t<q\), its cardinality is strictly greater than the stable image cardinality, so maximum preperiod is exactly \(q\).

**4. Entrance times and Koopman Jordan blocks.** Let \(R_t=|F^t(X)|\), where \(X\) is the full finite state space. Since every state enters a periodic orbit by time \(q\), each component is a rooted in-tree feeding a cycle. In the primary decomposition from Step 3, a vector has entered the periodic part exactly when its \(q\)-dimensional nilpotent primary coordinate is zero. Its first entrance at time \(t\ge1\) means this coordinate lies in \(\ker D^t\setminus\ker D^{t-1}\), where \(D=I+S\). For \(1\le t\le q\), this difference has cardinality \(2^t-2^{t-1}=2^{t-1}\). Independently there are \(2^{m-q}\) choices of the invertible primary coordinate, and two disjoint support parity classes for each nonzero nilpotent coordinate. Hence the number of states whose preperiod is exactly \(t\) is \(2\cdot2^{m-q}2^{t-1}=2^{m-q+t}\). All states outside \(U\) have preperiod zero.

The image of the Koopman operator \(K^t\) consists of complex functions constant on fibres of \(F^t\). Therefore \(\operatorname{rank}K^t=R_t\). The stabilization of these ranks implies that the zero generalized eigenspace has dimension \(R_0-R_q\), while the complement acts invertibly and, on the stabilized finite state image, as a permutation operator. For a nilpotent Jordan decomposition, the number of blocks of **exact** length \(t\) is
\[
 b_t=R_{t-1}-2R_t+R_{t+1}.
\]
Insertion of the formula for \(R_t\), including the stabilized range \(t\ge q\), gives the block multiplicities stated in the finding. The other eigenvalues arise from a finite permutation and are roots of unity.

## Verification

A standalone, standard-library checker (`verify.py`) reproduces the finite-state update and the twelve-vertex collision graph. Running `python3 verify.py` prints `VERIFY_OK states_examined_even= 87376 ring_sizes=3..16 offdiagonal_pair_vertices= 12 cyclic_pair_components= 2`. For every ring size from \(3\) through \(16\), it tests the image-rank hierarchy, entrance-time census, zero-Jordan multiplicities and permutation claim by exhaustive enumeration. These finite checks are supplementary: the polynomial-factorization and finite collision-graph arguments prove the statements for arbitrary ring sizes.

## Relationship to prior work

Zhu and Richard (2026, arXiv:2610.10967v1) formulate finite periodic Koopman analysis for elementary cellular automata and report that rule 154 has an exactly unitary odd-ring Koopman operator and nearly unitary even-ring examples, without specifying a general even-ring rank, transient, or zero-Jordan law. Nobe and Yura (2007) study rule 154 using linearization **on odd-size rings**, proving results about cycles in that restricted regime. Earlier periodic-boundary reversibility work identifies the odd-ring invertibility phenomenon. None of these inspected statements implies the explicit even-ring distribution of entrance times and nilpotent Koopman blocks. Distinct finite-ring parity-automaton and different elementary-rule enumerations concern different local maps and therefore do not imply the present theorem.

## Limitations

The classification is restricted to rule 154 with periodic boundaries and binary states, with \(N\ge3\). It does not classify the individual nonzero Koopman eigenvalue multiplicities or limiting infinite-volume spectra. Historical priority under another description of the exceptional alternating-support sector cannot be ruled out. External independent validation has not been performed.

## References

1. Q. Zhu and S. Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations*, arXiv:2610.10967v1 (publicly posted 2026-10-07), https://arxiv.org/abs/2610.10967.
2. A. Nobe and F. Yura, *Linearizable cellular automata*, Journal of Physics A 40 (2007), https://doi.org/10.1088/1751-8113/40/26/004.
3. Earlier literature on reversibility with periodic boundary conditions is discussed in the two sources above; no theorem from it on the stated even-ring transient/Jordan census is assumed.
