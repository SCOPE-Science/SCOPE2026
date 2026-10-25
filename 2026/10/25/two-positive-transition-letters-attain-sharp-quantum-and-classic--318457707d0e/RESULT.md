# Two positive transition letters attain sharp quantum and classical bounded-word Hankel identification laws

## Finding

For each \(D\geq1\), \(T\geq0\), and \(q\geq1\), let \(N_{\mathsf X,q}(D,T;\lambda_1,\lambda_2)\) be the largest number \(N\) of distinct prefix words \(u_j\) and suffix words \(v_i\), each of length at most \(T\) over the same \(q\)-letter alphabet, in a common \(D\)-state realization of class \(\mathsf X\), for which the acceptance table
\[
 h(u_jv_i)\geq1-\lambda_1\quad(i=j),\qquad h(u_jv_i)\leq\lambda_2\quad(i\ne j).
\]
The classes are \(\mathsf P\) (permutations of \(D\) points), \(\mathsf S\) (stochastic maps), \(\mathsf U\) (unitary conjugations on a \(D\)-dimensional Hilbert space), and \(\mathsf Q\) (completely positive trace-preserving maps). The common root distribution/density operator and the common terminal acceptance indicator/effect may be optimized with the transitions.

**Theorem (sharp binary alphabet).** Fix \(0\leq\lambda_1\), \(0<\lambda_2\), \(\lambda_1+\lambda_2<1\). Uniformly above a threshold depending only on the margins,
\[
\ln N_{\mathsf U,2}(D,T;\lambda_1,\lambda_2)
=\Theta_{\lambda_1,\lambda_2}(\min\{D^2,T\}),\qquad
\ln N_{\mathsf P,2}(D,T;\lambda_1,\lambda_2)
=\Theta_{\lambda_1,\lambda_2}(\min\{D,T\}).
\]
The same respective laws hold for \(\mathsf Q\) and \(\mathsf S\) by inclusion and the general packing upper bounds. When \(\lambda_2=0\), \(0\leq\lambda_1<1\), all four classes satisfy
\[
\ln N_{\mathsf X,2}(D,T;\lambda_1,0)=\Theta(\min\{\ln D,T\}).
\]
Two input letters are minimal for the positive-tolerance laws. In particular, the fixed four-letter lower bounds of Zhao (2026), available from October 15, 2026, transfer to a strictly binary positive alphabet with an explicit dimension factor \(18\) and word-length factor \(26\).

## Assumptions and scope

The alphabet consists of positive input symbols; formal inverse symbols cannot be read directly. Transition maps may depend on \(D,T\) and the margins. Every row and column is indexed by a possibly different word of length at most \(T\), but all words share the same two transitions, root, and terminal measurement. For the quantitative reduction below, \(N_{\mathsf X,q}\) retains this definition even when the dimensions or horizon are below the eventual asymptotic threshold. The source paper's type-I/type-II convention is used throughout.

## Proof

**Lemma 1 (compress any fixed alphabet to two reversible maps).** For \(m\geq2\) and unitary maps \(G_0,\ldots,G_{m-1}\) on a \(d\)-dimensional Hilbert space, there exist two unitaries \(S,T\) on a space of dimension \(6(m-1)d\), an embedded \(d\)-dimensional core \(H_0\), and nonempty binary words \(c_0,\ldots,c_{m-1}\) satisfying: each \(c_j\) maps \(H_0\) to itself and acts there as \(G_j\); each word has length at most
\[
 L_m=\max\{4(m-1),\,10(m-2)+6\}.
\]
If the \(G_j\) are real orthogonal, so are \(S,T\); if they are permutations, so are \(S,T\).

*Proof.* Put \(r=m-1\) and first use \(r\) copies \(H_0\oplus\cdots\oplus H_{r-1}\) of the original space. Define \(A\) by \((j,x)\mapsto(j+1,x)\) for \(0\leq j<r-1\) and \((r-1,x)\mapsto(0,G_0x)\); define \(B\) on \(H_j\) by \(G_{j+1}\). These are unitaries, orthogonals, or permutations in their respective cases. Under the chronological convention that a word's first symbol acts first, \(a^r\) acts on \(H_0\) as \(G_0\), and \(a^jb a^{-j}\) acts there as \(G_{j+1}\) for \(0\leq j<r\); all return to \(H_0\). The negative powers at this stage are symbolic inverses, which we now replace by positive binary words.

Let \(K\) be the \(rd\)-dimensional space of \(A,B\). Take six copies \(U_0,U_1,U_2,V_0,V_1,V_2\) of \(K\). Define \(T\) to cycle each triple forward, so \(T^3=I\). Let \(C_0=I\), \(C_1=B^{-1}\), \(C_2=A^{-1}\), and define \(S\) by exchanging \(U_j(x)\) with \(V_{-j}(C_jx)\), with label indices modulo \(3\); on the reverse direction \(V_{-j}(y)\mapsto U_j(C_j^{-1}y)\). Hence \(S^2=I\) and both \(S,T\) have the claimed preservation properties.

Starting from \(U_0\), direct tracking of the six labels gives the following *positive* binary implementations of the stage-one actions on the whole of \(U_0\):

| Stage-one operation | Positive word | Length |
| --- | --- | ---: |
| \(A\) | `stst` | 4 |
| \(A^{-1}\) | `ttstts` | 6 |
| \(B\) | `sttstt` | 6 |
| \(B^{-1}\) | `tsts` | 4 |

Indeed, `stst` visits \(U_0,V_0,V_1,U_2,U_0\) and applies \(C_2^{-1}=A\); `sttstt` visits \(U_0,V_0,V_1,V_2,U_1,U_2,U_0\) and applies \(C_1^{-1}=B\). The inverse words follow from \(S^2=T^3=I\), and also preserve \(U_0\). Substitute these words for \(a,a^{-1},b,b^{-1}\) in the first-stage macros. The word for \(G_0\) has length \(4r\); the word for \(G_{j+1}\) has length \(4j+6+6j=10j+6\). These give \(L_m\). Every macro preserves the nested original \(d\)-dimensional core; concatenation therefore preserves *every* original word product, without approximation. \(\square\)

**Lemma 2 (acceptance-table embedding).** For \(D\geq6(m-1)\) and \(T\geq L_m\), let \(d=\lfloor D/[6(m-1)]\rfloor\) and \(t=\lfloor T/L_m\rfloor\). Then
\[
N_{\mathsf P,2}(D,T;\lambda_1,\lambda_2)\geq
N_{\mathsf P,m}(d,t;\lambda_1,\lambda_2),
\]
with the identical statement for \(\mathsf U\).

*Proof.* Apply Lemma 1 to the selected realization's transition tuple. Replace each source prefix and suffix by the concatenation of the corresponding binary macros. Their lengths are at most \(L_m t\leq T\), and every product agrees on the invariant core. Extend the original root and terminal test by zero off the core, so all acceptance probabilities remain identical. Unused dimensions are padded by fixed states or an orthogonal identity sector. The binary row and column word families remain distinct: if two were equal, their acceptance-table rows or columns would be equal, contradicting the strict gap \(1-\lambda_1>\lambda_2\) for \(N\geq2\). For \(N=1\) the assertion is immediate. \(\square\)

**Sharp growth.** With \(m=4\), Lemma 2 gives the explicit domination
\[
N_{\mathsf X,2}(D,T;\lambda_1,\lambda_2)\geq
N_{\mathsf X,4}(\lfloor D/18\rfloor,\lfloor T/26\rfloor;\lambda_1,\lambda_2)
\quad(\mathsf X\in\{\mathsf P,\mathsf U\}),
\]
for \(D\geq18,T\geq26\). Zhao's four-letter theorem supplies the \(\Omega(\min\{d^2,t\})\) unitary and \(\Omega(\min\{d,t\})\) permutation lower bounds, and the general stochastic/CPTP converse bounds supply matching \(O(\min\{D,T\})\) and \(O(\min\{D^2,T\})\) upper bounds for *any fixed alphabet*, including two letters. Since division by constants changes these minima only by bounded factors above a fixed threshold, the claimed two-letter scaling laws follow. Inclusion \(\mathsf P\subseteq\mathsf S\) and \(\mathsf U\subseteq\mathsf Q\) extends the lower bounds. At zero false acceptance, transfer Zhao's four-letter \(\Omega(\min\{\ln d,t\})\) constructions through the same lemma, while exclusive-support and word-count upper bounds give \(N\leq D\) and \(N\leq2^{T+1}-1\); hence the asserted zero-tolerance law.

**Minimal alphabet.** On a unary alphabet, only the words of lengths \(0,1,\ldots,T\) are possible as distinct prefixes, giving \(N_{\mathsf X,1}(D,T)\leq T+1\), regardless of carrier dimension. Take \(D=T\to\infty\): the positive-tolerance two-letter lower bounds above yield logarithmic identification sizes of order \(T\), which no unary alphabet can provide. Thus two is the least alphabet size attaining both sharp dimension–horizon laws. \(\square\)

## Verification

The accompanying `verify.py` checks the block matrices and positive substitution words on random permutation matrices and Haar-distributed unitaries, for original dimensions \(2,3,4\) and alphabet sizes \(2,3,4,5\). It verifies the generator involution/order identities, invariance and the exact action on the core of every substituted letter and selected longer original words; it checks the announced dimensions and word-length bounds. `verification_output.txt` contains the reproducible `VERIFY_OK` result. The proof of all-dimensional correctness is the explicit label tracking above; the finite tests only detect implementation errors and do not establish the asymptotic law.

## Relationship to prior work

Yixin Zhao, *Controlled-Memory Identification with Shared Generators: Dimension–Horizon Tradeoffs and Quantum–Classical Separation* (arXiv:2610.21797v1, first public October 15, 2026), Theorems II.2 and II.3, establishes the four-letter bounds and explicitly leaves the minimum alphabet cardinality, specifically whether two or three symbols suffice, open in Section VIII-D. The revision *Hankel Submatrices with Bounded Word Length: Dimension Tradeoffs in Probabilistic and Quantum Automata* (arXiv:2610.21797v2, October 19, 2026) reformulates the same fixed-margin conclusion as an approximate identity submatrix of the acceptance Hankel matrix and reiterates this open problem in Section 7.4. The present reduction preserves the required common-root/common-terminal response table; it does not assert that the four-letter source theorem or elementary free-group code techniques are original.

Birget and Margolis, *Two-letter group codes that preserve aperiodicity of inverse finite automata* (arXiv:math/0701264v1, 2007), Proposition 2.6, already gives signed two-letter free-group encodings by conjugates. Its inverse-automaton language/folding reductions do not by themselves implement each letter as a *positive* input word over two reversible transitions with a uniform constant-factor Hilbert-space enlargement and unchanged unitary/permutation acceptance tables. In particular, the involution/order-three gadget supplies an additional positive-input realization absent from the cited group-code theorem. This comparison distinguishes the narrower elementary group-encoding ingredient from the quantitative fixed-margin Hankel conclusion.

## Limitations

The dimension and word-length overheads \(18\) and \(26\) are explicit sufficient constants, not claimed optimal. The theorem concerns optimized generator tuples rather than a prescribed fixed pair, positive finite alphabets, and exact reversible transitions; it does not address noisy or circuit-local gate synthesis. Independent checking of literature novelty and of the inherited four-letter theorem is still appropriate. A prior unindexed reduction achieving the same transfer remains possible.

## References

1. Y. Zhao, *Controlled-Memory Identification with Shared Generators: Dimension–Horizon Tradeoffs and Quantum–Classical Separation*, arXiv:2610.21797v1 (October 15, 2026), https://arxiv.org/abs/2610.21797v1.
2. Y. Zhao, *Hankel Submatrices with Bounded Word Length: Dimension Tradeoffs in Probabilistic and Quantum Automata*, arXiv:2610.21797v2 (October 19, 2026), https://arxiv.org/abs/2610.21797v2.
3. J.-C. Birget and S. W. Margolis, *Two-letter group codes that preserve aperiodicity of inverse finite automata*, arXiv:math/0701264v1 (2007), https://arxiv.org/abs/math/0701264v1.
