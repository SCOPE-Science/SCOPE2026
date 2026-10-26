# Exact spatial image language and entropy of elementary cellular automaton Rule 110

## Finding

For the binary radius-one Rule 110 cellular automaton \(\Phi\), let \(Y=\Phi(\{0,1\}^{\mathbb Z})\) be its **one-step spatial image**. Write \(a_n=|\mathcal L_n(Y)|\) for the number of allowed length-\(n\) spatial words, with \(a_0=1\). Then, exactly,

\[
\sum_{n\ge0}a_n z^n=\frac{1-z+z^2}{(1-z)(1-2z+z^2-z^3-z^4)}.
\]

In particular, \((a_0,\ldots,a_{12})=(1,2,4,8,16,31,59,112,213,405,769,1459,2768)\). The spatial topological entropy is

\[
h_{\mathrm{top}}(\sigma|_Y)=\log\lambda=0.6403682574172238\ldots,
\qquad \lambda=1.897179401065394\ldots,
\]

where \(\lambda\) is the unique largest positive root of \(\lambda^4-2\lambda^3+\lambda^2-\lambda-1=0\). Moreover, the image \(Y\) is sofic but **not a shift of finite type**: every word \(0\,1\,0^m\,1\,0\), for integer \(m\ge1\), is a minimal forbidden word. The five-state deterministic presentation below recognizes its entire finite language, not just sample output blocks.

## Assumptions and scope

The local Rule 110 function is \(f(a,b,c)=\lfloor 110/2^{4a+2b+c}\rfloor\bmod2\), for \(a,b,c\in\{0,1\}\). Equivalently, in neighborhood order \(111,110,101,100,011,010,001,000\), the eight outputs are \(0,1,1,0,1,1,1,0\). The shift \(\sigma\) acts by spatial translation on bilateral configurations. All assertions concern the image under **one application** of \(\Phi\), not the long-time image intersection \(\bigcap_{t\ge1}\Phi^t(\{0,1\}^{\mathbb Z})\), temporal traces, or the entropy of \(\Phi\) as a time-evolution map.

## Proof

**1. An exact four-state labeled path presentation.** Use vertices \(00,01,10,11\), interpreted as integers \(0,1,2,3\). For each triple \(abc\) include an edge from \(ab\) to \(bc\) labeled \(f(a,b,c)\). The zero-labeled edges, written as (source,target), are exactly \((0,0),(2,0),(3,3)\); the one-labeled edges are \((0,1),(1,2),(1,3),(2,1),(3,2)\). A finite word \(w\) is in \(\mathcal L(Y)\) if and only if it labels a finite path, since the corresponding finite preimage block can be extended arbitrarily to a bilateral input. This establishes the exact image-language recognition claim without any mixing or recurrence assumption.

**2. Determinization and minimization.** Starting from the full vertex set \(\{0,1,2,3\}\), apply a letter to a subset by taking the union of its labeled successors. Exactly eight subsets, including the empty subset, are reachable. Group the seven nonempty subsets as

\[
\begin{array}{c|l}
A&\{0,1,2,3\},\ \{1,2,3\}\\
B&\{0,3\},\ \{2,3\}\\
C&\{1,2\}\\
D&\{0\}\\
E&\{1\}
\end{array}
\]

The two subsets within each of the first two classes have identical right languages: the maps on symbols \(0,1\) induce the same quotient transitions. Consequently the following deterministic automaton is exact, with initial state \(A\), all five displayed states accepting, and a rejecting dead state for absent edges:

\[
\begin{array}{c|cc}
&0&1\\\hline
A&B&A\\ B&B&C\\ C&D&A\\ D&D&E\\ E&\varnothing&B
\end{array}
\]

For completeness, the five accepting states are pairwise distinguishable by right-language suffixes of length at most eight (also checked exactly in the accompanying verifier), so this is the minimal complete deterministic language automaton after adding the dead state. This finite automaton proves that \(Y\) is sofic.

**3. Exact growth.** In state order \((A,B,C,D,E)\), the adjacency matrix, counting distinct labeled transitions of the deterministic automaton, is

\[
M=\begin{pmatrix}
1&1&0&0&0\\
0&1&1&0&0\\
1&0&0&1&0\\
0&0&0&1&1\\
0&1&0&0&0
\end{pmatrix}.
\]

Since each admitted word labels exactly one path from \(A\), \(a_n=e_A^{\mathsf T}M^n\mathbf 1\), including \(n=0\). Solving \((I-zM)v=\mathbf1\) gives

\[
v_A=\frac{1-z+z^2}{(1-z)(1-2z+z^2-z^3-z^4)}.
\]

Equivalently \(\det(tI-M)=(t-1)(t^4-2t^3+t^2-t-1)\). Every state is accessible from \(A\), the directed graph is strongly connected, and it has a loop at \(A\), hence \(M\) is primitive. Perron–Frobenius theory therefore gives \(a_n\sim c\lambda^n\) for a positive constant \(c\), where \(\lambda\) is the Perron eigenvalue. The quartic has precisely one positive root above \(1\), and its largest-modulus root is \(\lambda\), by primitivity. It follows that the spatial word-growth entropy is \(\log\lambda\). The exact generating function additionally determines every finite block count.

**4. Strict soficity.** For every integer \(m\ge1\) put \(w_m=01\,0^m\,10\). Its deterministic path from \(A\) goes \(A\overset0\to B\overset1\to C\overset0\to D\), stays at \(D\) on any remaining zeros, then follows \(D\overset1\to E\), and finally takes the forbidden transition \(E\overset0\to\varnothing\). Thus \(w_m\) is forbidden. Its immediate prefix \(01\,0^m\,1\) ends at \(E\) and its immediate suffix \(1\,0^m\,10\) ends at \(D\), so both are allowed. Every proper contiguous factor is contained in one of those two words. Hence \(w_m\) is minimal forbidden. Their lengths tend to infinity. A shift of finite type has a uniform bound on lengths of minimal forbidden words (after reducing its finite forbidden list); this contradicts the constructed family. Thus \(Y\) is not of finite type.

## Verification

The self-contained `verify.py` reconstructs all labeled de Bruijn edges from the actual Rule 110 local rule, computes the reachable subset automaton independently, checks the five-class quotient, distinguishes all pairs of deterministic states, and exhaustively compares accepted words against all length-\(n+2\) preimage blocks through \(n=10\). It also checks 21 exact coefficients against the displayed generating function and verifies 149 instances of the minimal forbidden-word pattern. The infinite statements follow from the exact automaton identity, matrix computation, Perron theory, and all-integer minimality argument; finite enumeration by itself is not their proof.

## Relationship to prior work

Jen (1989) gives a general framework for finite-preimage enumeration of elementary cellular automata and examines image-language restrictions for multiple rules, including complete descriptions of different rules. That general machinery motivates the calculation but, in inspected passages, does not display this five-state Rule-110 image automaton, rational generating function, or strict-sofic witness family. Cook (2004) proves the temporal computational universality of Rule 110, which does not entail the evaluated one-step spatial image language or entropy. There is no assertion that automaton determinization, entropy from Perron roots, or soficity criteria are themselves new. This is an explicit specialization and evaluation for a canonical rule, with priority uncertainty noted below.

## Limitations

This result does not compute Rule 110's temporal topological entropy, its long-time limit set, the distribution of output words under a prescribed input measure, or its periodic preimage structure. The derivation is elementary automata theory applied to a classical rule; older rule-specific tables or unindexed catalogues could contain an equivalent evaluation. Historical priority has not been independently certified. Numerical decimals are derived from the exact algebraic expressions and are not required for proof.

## References

1. Matthew Cook, *Universality in Elementary Cellular Automata*, Complex Systems **15** (2004), 1–40, DOI: 10.25088/ComplexSystems.15.1.1, publicly dated 2004-03-15; https://www.complex-systems.com/abstracts/v15_i01_a01/ .
2. Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456; https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
