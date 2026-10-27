# An exact least-common-multiple barrier to finite-period entropy identification

## Finding

Fix integers \(\kappa\ge2\) and \(m\ge1\). In the two-sided full shift on the alphabet \(\mathbb Z/\kappa\mathbb Z\), define \(X_{\kappa,m}\) by requiring
\[
y_i=x_{i+m}-x_i\pmod\kappa\in\{0,1\},\qquad y_i y_{i+1}=0\quad (i\in\mathbb Z).
\]
Then \(X_{\kappa,m}\) is a **mixing shift of finite type** with topological entropy \(\log\varphi\), where \(\varphi=(1+\sqrt5)/2\). Moreover, for every \(n\ge1\),
\[
|\operatorname{Fix}(\sigma^n\mid X_{\kappa,m})|=\kappa^n\quad\Longleftrightarrow\quad n\mid m.
\]
Therefore, given any finite observation horizon \(H\ge1\), the fixed-point counts of all iterates \(1,\ldots,H\), equivalently all primitive-orbit counts to that cutoff, agree exactly with those of the full \(\kappa\)-shift if and only if \(\operatorname{lcm}(1,\ldots,H)\mid m\). The sharp minimum delay is \(\operatorname{lcm}(1,\ldots,H)\). Consequently the associated Artin–Mazur zeta series agree through degree \(H\) even though their entropies differ by the fixed positive amount \(\log\kappa-\log\varphi\).

## Assumptions and scope

All shifts are two-sided, with the usual product topology; fixed-point counts are for the shift map \(\sigma\), not for time evolution of a cellular automaton. The alphabet is \(\mathbb Z/\kappa\mathbb Z\), and the only allowed difference symbols are the residues \(0\) and \(1\). The output difference shift is the binary golden-mean shift \(Y=\{y\in\{0,1\}^{\mathbb Z}: y_i y_{i+1}=0\}\). The construction is a finite-to-one preimage under the lag-\(m\) permutative difference block code; it is not claimed to be a fixed-memory family as \(H\to\infty\).

## Proof

**Finite type, finite-to-one factor, and entropy.** The defining conditions forbid finitely many blocks of length at most \(m+2\), so \(X_{\kappa,m}\) is an SFT. The sliding-block map \(\pi_m(x)_i=x_{i+m}-x_i\pmod\kappa\) takes \(X_{\kappa,m}\) onto \(Y\): given any \(y\in Y\), assign the \(m\) coordinates \(x_0,\ldots,x_{m-1}\) arbitrarily in \(\mathbb Z/\kappa\mathbb Z\), then use \(x_{i+m}=x_i+y_i\) forwards and backwards. Every assignment extends uniquely, so each fiber contains exactly \(\kappa^m\) points. Finite-to-one factor maps between compact systems preserve topological entropy. The golden-mean shift has adjacency matrix \(\begin{pmatrix}1&1\\1&0\end{pmatrix}\), with Perron eigenvalue \(\varphi\); hence \(h_{\mathrm{top}}(X_{\kappa,m})=\log\varphi\).

**Mixing.** Use a one-step graph whose vertices are \((u,e)\in(\mathbb Z/\kappa\mathbb Z)^m\times\{0,1\}\), where \(u=(x_i,\ldots,x_{i+m-1})\) and \(e=y_{i-1}\). An edge labeled \(a\in\{0,1\}\) is allowed if \(ea=0\) and sends the state to
\[
(u_1,\ldots,u_{m-1},u_0+a;\ a).
\]
Every vertex occurs in the presented shift, because permissible one-sided output sequences can be extended in both directions by the invertible recurrence. For any two vertices and every sufficiently large prescribed path length \(T\), we can choose \(a_0,\ldots,a_{T-1}\in\{0,1\}\) with no neighboring ones, compatible with the initial and final \(e\)-symbols, so that the prescribed final \(m\)-block is reached. Indeed, in a window of length \(T\), each pulse \(a_t=1\) increments exactly one of the \(m\) initial residue classes \(t\bmod m\) (viewed in the cyclically rotated final block). Fix an initial zero and the required last symbol. Well inside the window, reserve \(m\) mutually disjoint long time blocks, one for each residue class. In its block choose, at mutually nonadjacent times in the prescribed residue class, a number of isolated pulses realizing the required residue increment modulo \(\kappa\). The last forced pulse, when present, is subtracted from the target increment in that residue class. Each block can accommodate \(\kappa\) pulses, and all boundaries are padded by zeros; this works for every sufficiently large \(T\), including \(m=1\) by using alternate sites. Thus the graph admits paths of every sufficiently large length between every pair of vertices. Its adjacency matrix is primitive, proving that \(X_{\kappa,m}\) is mixing.

**Exact period criterion.** Every \(n\)-periodic \(x\) is a word of length \(n\) repeated bi-infinitely. There are exactly \(\kappa^n\) such points in the ambient full shift. If \(n\mid m\), then \(x_{i+m}=x_i\) for all \(i\), so all these points have \(y_i=0\) and belong to \(X_{\kappa,m}\).

Conversely suppose \(n\nmid m\) and let \(r=m\bmod n\), with \(1\le r<n\). If \(\kappa\ge3\), take the periodic word with a single coordinate equal to \(1\) and all others \(0\). At the coordinate of that \(1\), its lag-\(r\) difference equals \(-1\pmod\kappa=\kappa-1\), not one of the allowed residues. If \(\kappa=2\), choose a binary \(n\)-periodic word satisfying the two equations
\[
x_r-x_0=1\pmod2,\qquad x_{1+r}-x_1=1\pmod2.
\]
Such a word always exists: these are parity constraints on two nonloop edges in the graph of residue indices modulo \(n\), with equal right-hand sides; a two-edge graph has no inconsistent odd cycle (if the two edges coincide, the equations agree). Its output has the forbidden adjacent pair \(y_0=y_1=1\). Hence for every \(n\nmid m\), at least one ambient \(n\)-periodic point is excluded, proving strict inequality and the equivalence.

**Optimal observation horizon.** Equality for each \(n=1,\ldots,H\) is equivalent to simultaneous divisibility of \(m\) by every such \(n\), or \(\operatorname{lcm}(1,\ldots,H)\mid m\). The minimal positive such \(m\) is precisely that least common multiple. By Möbius inversion, fixed-period counts determine primitive-orbit counts through \(H\). Finally, the formal Artin–Mazur zeta function is
\[
\zeta_X(z)=\exp\left(\sum_{n\ge1}\frac{|\operatorname{Fix}(\sigma^n\mid X)|}{n}z^n\right).
\]
Its coefficients through degree \(H\) therefore agree with \(1/(1-\kappa z)\), the full-shift zeta function, although the full-shift entropy is \(\log\kappa>\log\varphi\).

## Verification

The arguments are symbolic and apply to all \(\kappa,m,n,H\) in the stated ranges. An independent finite checker exhaustively verified the full-shift equality criterion for \(\kappa\in\{2,3,4\}\) and \(1\le m,n\le6\). It also verified the explicit residue-sum formula for \(\kappa\in\{2,3,4\}\), selected lags, and \(1\le n\le6\); these are supplementary checks, not substitutes for the infinite proof. See `CHECK.py` for a self-contained executable verification.

## Relationship to prior work

Kang and Jäger (arXiv:2609.01140v1) introduce the same family of permutative difference codes and study minimality and unique ergodicity when lifting aperiodic substitution and Toeplitz subshifts. Here the base is instead a mixing positive-entropy golden-mean SFT, and the conclusion is an exact finite-period/entropy nonidentifiability law with sharp least delay. Mariot, Leporati, Dennunzio, and Formenti analyze periods of preimages under surjective cellular automata and give general period-computation procedures; the new claim is the joint mixing/entropy-gap/finite-observation equivalence and its least-common-multiple barrier, not a claim of inventing preimage-period algorithms. MacDonald's theorem on encoding through sliding block codes gives periodic-point conditions for embeddings, not this fixed-entropy obstruction.

## Limitations

The memory \(m+1\) and the finite-to-one fiber degree \(\kappa^m\) increase when the matched observation horizon increases. The result does not imply the same indistinguishability with a uniformly bounded memory or degree, nor under smoothness constraints. Known preimage-period algorithms may indirectly recover individual counting ingredients; the literature-priority assessment concerns the complete sharp mixing/entropy-gap barrier and is not an independent novelty certification.

## References

1. Z. Kang and T. Jäger, *On lifts of strictly ergodic subshifts by permutative sliding block codes*, arXiv:2609.01140v1 (first public date 2026-09-01), primary classification 37B10; https://arxiv.org/html/2609.01140v1.
2. L. Mariot, A. Leporati, A. Dennunzio, and E. Formenti, *Computing the periods of preimages in surjective cellular automata*, *Natural Computing* 16 (2017), 367–381, DOI: 10.1007/s11047-016-9586-x; author postprint https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf.
3. R. MacDonald, *Encoding subshifts through sliding block codes*, *Ergodic Theory and Dynamical Systems*, online 2023; https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/encoding-subshifts-through-sliding-block-codes/861CDCF1FD91F8CEFD86C9C8C3A448D8.
4. D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995.
