# The two-block Moran-forest partition law and logarithmically uniform component scales

## Finding

Consider the stationary Moran forest on the labeled set \(\{1,\ldots,n\}\) of Bienvenu, Duchamps, and Foutel-Rodier. Write \(\Pi_n\) for its partition into connected components and \(K_n\) for the number of components. For every integer \(n\ge3\) and every prescribed unordered bipartition \(\{A,B\}\), where \(|A|=a\ge1\), \(|B|=b\ge1\), and \(a+b=n\), one has the exact **two-block exchangeable partition probability**

\[
\Pr\{\Pi_n=\{A,B\}\}=
\frac{(a-1)!(b-1)!(n^2-1)(ab-1)}
{(n-1)^n(a+1)(b+1)}.
\]

Condition on the rare event \(K_n=2\), and write \(S_n\) for the smaller of the two component sizes. Set, for \(1\le s\le\lfloor n/2\rfloor\),

\[
\begin{aligned}
w_n(s)&=\frac{(n+1)(s(n-s)-1)}{s(n-s)(s+1)(n-s+1)},\\
c_n(s)&=\begin{cases}1,&2s<n,\\1/2,&2s=n,\end{cases}\\
Z_n&=\frac{(n-1)H_{n-2}-(n-2)}{n},\qquad
H_m=\sum_{j=1}^m\frac1j.
\end{aligned}
\]

Then the exact conditional law and the scaling limit are

\[
\Pr\{S_n=s\mid K_n=2\}=\frac{c_n(s)w_n(s)}{Z_n},
\qquad
\frac{\log S_n}{\log n}\ \bigg|\ (K_n=2)
\ \xrightarrow[]{\mathrm d}\ \operatorname{Unif}[0,1].
\]

In particular, the smaller component is typically on a random polynomial scale rather than a constant, a fixed fraction of the vertices, or a single deterministic power of \(n\).

## Assumptions and scope

The stationary Moran forest is the invariant law of the vertex-deletion-and-reattachment process on a complete labeled vertex set, where the updated vertex and its attachment partner are selected uniformly among ordered distinct pairs. Components are counted after ignoring edge orientations. The event \(K_n=2\) has positive probability for each integer \(n\ge3\). The probability of a prescribed unordered bipartition is for exactly two components and includes their vertex labels. At equal sizes, \(A\) and \(B\) must not be double-counted. The limit is weak convergence under the conditional law, not an unconditional statement about typical forests.

## Proof

**1. Independent-parent representation.** The uniform-attachment representation (Proposition 2.1 of [1]) orders births as \(1,\ldots,n\) and independently chooses \(U_j\) uniformly from \(\{1,\ldots,n\}\setminus\{j\}\). An edge joins \(j\) to \(U_j\) precisely if \(U_j<j\). A final independent uniform permutation of all labels gives the stationary Moran forest. Each independent-parent vector has probability \((n-1)^{-n}\).

**2. Count two prescribed components.** Fix a partition \(\{A,B\}\) of sizes \(a,b\), and condition on their uniformly random positions in the birth order. For any fixed interleaving, every nonfirst member of \(A\) must attach to an earlier member of \(A\), and similarly for \(B\). This gives exactly \((a-1)!(b-1)!\) allowable parent choices, independent of the interleaving. The earliest member of each block must be a root, and thus must choose a later birth position. If their birth positions are \(r_A,r_B\), the number of allowable choices at these two roots is \((n-r_A)(n-r_B)\). This also proves that the counted assignments produce precisely the two desired components: each block has a unique root and every other member connects to an earlier member within the same block.

Let \(W\) denote the initial length of the run of one block in the uniformly shuffled binary word of \(a\) letters of one type and \(b\) of the other. The first of the two roots is born at position one, the other at \(W+1\); the root-choice factor is therefore \((n-1)(n-1-W)\). In a random word, the expected number of \(A\)-letters before the first \(B\)-letter is \(a/(b+1)\), and symmetrically the expected number of \(B\)-letters before the first \(A\)-letter is \(b/(a+1)\). Exactly one such count is positive, so

\[
\mathbb E W=\frac{a}{b+1}+\frac{b}{a+1}.
\]

A direct algebraic simplification yields

\[
\mathbb E[(n-r_A)(n-r_B)]
=(n-1)\left(n-1-\frac{a}{b+1}-\frac{b}{a+1}\right)
=\frac{(n^2-1)(ab-1)}{(a+1)(b+1)}.
\]

Multiplying by \((a-1)!(b-1)!/(n-1)^n\) proves the bipartition formula. Relabeling does not alter the probability because the construction is exchangeable.

**3. Exact conditional mass.** If \(s<n/2\), there are \(\binom ns\) distinct labeled bipartitions with smaller part \(s\). If \(s=n/2\), there are half that many. Using

\[
\binom ns(s-1)!(n-s-1)!=\frac{n!}{s(n-s)}
\]

shows that

\[
\Pr\{S_n=s,K_n=2\}=
\frac{n!}{(n-1)^{n-1}}c_n(s)w_n(s).
\]

The root indicators for birth positions \(j\) are independent, with root probabilities \((n-j)/(n-1)\). Birth position one is always a root and position \(n\) never is. Hence exactly one additional root occurs with probability

\[
\begin{aligned}
\Pr\{K_n=2\}
&=\frac{(n-2)!}{(n-1)^{n-2}}
\sum_{j=2}^{n-1}\frac{n-j}{j-1}\\
&=\frac{(n-2)!}{(n-1)^{n-2}}
\big((n-1)H_{n-2}-(n-2)\big).
\end{aligned}
\]

Dividing the joint probability by this strictly positive expression gives the stated conditional mass, including the equal-size correction. It also proves the normalization identity \(\sum_s c_n(s)w_n(s)=Z_n\).

**4. The logarithmic scale.** For \(1\le s\le n/2\), let \(b=n-s\). The exact rearrangement

\[
w_n(s)=\frac{n+1}{n+2}\left(1-\frac1{sb}\right)
\left(\frac1{s+1}+\frac1{b+1}\right)
\]

shows uniformly in this range that \(w_n(s)=1/(s+1)+O(1/n)\), because \(b\ge n/2\) and \(sb\ge n-1\). Also, \(Z_n=\log n+O(1)\). Fix \(0<x<1\). Eventually \(\lfloor n^x\rfloor<n/2\), so the exceptional equal-size factor is irrelevant. Therefore

\[
\Pr\{S_n\le n^x\mid K_n=2\}
=\frac{\sum_{s=1}^{\lfloor n^x\rfloor}(1/(s+1)+O(1/n))}{\log n+O(1)}
=\frac{x\log n+O(1)+O(n^{x-1})}{\log n+O(1)}\longrightarrow x.
\]

At \(x=0\) the mass on \(S_n=1\) is \(O(1/\log n)\), and for \(x\ge1\) the probability is one; the limiting distribution function is that of a uniform random variable on \([0,1]\). This proves weak convergence.

## Verification

The independent-parents model was enumerated using exact integer counts for all \((n-1)^n\) choice vectors at each order \(3\le n\le7\), comparing the complete two-component size profiles against the closed formula. The counts also match the independently derived number-of-roots law; these are unrestricted exhaustive finite tests, not an infinite proof. Exact rational checks confirm the conditional normalization identity for all \(3\le n\le100\). Reproduce using Python 3 standard library with `python verify.py`. The preceding algebra and uniform estimates prove the statements for all admissible orders and the infinite limit.

## Relationship to prior work

Bienvenu, Duchamps, and Foutel-Rodier [1] introduced the stationary Moran forest, proved its independent-parent representation and component-count distribution, and explicitly noted in Section 2.2 that they had not found a closed expression for its exchangeable partition probability function. Their Section 5 describes a uniformly sampled component and the largest component in the ordinary, unconditioned model. Here the result gives an exact **two-block** probability for a prescribed partition and a logarithmic rare-event scale law after conditioning on precisely two components. These are neither statements of [1] nor consequences of its unconditioned component-size limits. The later edit-semigroup treatment [2] studies transition spectra and mixing, not this finite partition probability. The general EPPF for arbitrary numbers of blocks is not claimed.

## Limitations

Only the sector with exactly two components is classified. This finding does not give a closed formula for the full multi-block partition law and does not determine conditional attachment-tree shapes beyond the source construction. Novelty assessment is based on the identified primary literature and indexed research searches, so historical priority beyond the inspected sources remains uncertain. The numerical verifier checks only finite cases; the proof of the weak limit is analytical.

## References

[1] F. Bienvenu, J.-J. Duchamps, and F. Foutel-Rodier, *The Moran forest*, arXiv:1906.08806, first posted 2019-06-20; Random Structures & Algorithms, DOI: 10.1002/rsa.20997. Author-available paper: https://www.normalesup.org/~bienvenu/articles/BienvenuRSA2021.pdf (particularly Proposition 2.1, Section 2.2, Proposition 3.1, Section 5).

[2] F. Chung and S. J. Robertson, *Stochastically Evolving Graphs via Edit Semigroups*, arXiv:2509.19678 (2025), especially its discussion of the Moran-forest edit process.
