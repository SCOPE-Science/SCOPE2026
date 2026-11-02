# Exact stabilization-time distribution for the cyclic three-site majority automaton

## Finding

For every integer \(n\ge1\), consider the synchronous Boolean majority map
\[
M_n:\{0,1\}^n\longrightarrow\{0,1\}^n,\qquad
(M_nx)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1}),
\]
with indices modulo \(n\), including the repeated-neighbor cases at \(n=1,2\). This is elementary cellular automaton Rule 232. Define the first-fixed-state time \(\tau(x)\) to be the least \(t\ge0\) for which \(M_n^{t+1}x=M_n^tx\), if one exists; otherwise put \(\tau(x)=\infty\).

Write \(d_i=x_i\oplus x_{i+1}\) for the cyclic domain-wall word. Unless every \(d_i=1\), let \(q(x)\) denote the greatest length of a cyclic run of consecutive ones in \(d\), taking \(q=0\) when \(d\) is all zero. Then
\[
\boxed{\tau(x)=\left\lfloor q(x)/2\right\rfloor.}
\]
The sole nonconverging states are the two alternating words when \(n\) is even; they form one temporal two-cycle. Consequently, the largest finite hitting time on the \(n\)-ring is \(\lfloor(n-1)/2\rfloor\), and this bound is attained for every \(n\ge1\).

More strongly, for every integer \(t\ge0\), let \(F_{n,t}\) count the indexed words \(x\in\{0,1\}^n\) with \(\tau(x)\le t\). With \(L=2t+1\), put
\[
Q_L(u,z)=1-\sum_{j=0}^{L}u^jz^{j+1}.
\]
Then the complete finite-size/finite-time cumulative distribution has the exact rational generating function
\[
\boxed{\sum_{n\ge1}F_{n,t}z^n=
-z\frac{d}{dz}\log\!\left(Q_{2t+1}(1,z)Q_{2t+1}(-1,z)\right).}
\]
The logarithmic derivative denotes an identity of formal power series; no analytic branch is needed. The number settling **at precisely** time \(t\) is \(F_{n,t}-F_{n,t-1}\) for \(t\ge1\), and is \(F_{n,0}\) at time zero. The two alternating states (when \(n\) is even) are excluded from every \(F_{n,t}\), as their hitting time is infinite.

## Assumptions and scope

The ring has labeled positions \(i\in\mathbb Z/n\mathbb Z\), with no quotient by rotations or color exchange. Every initial word has equal weight in the enumeration, and every site updates simultaneously using its own bit and its two cyclic neighbors. XOR, written \(\oplus\), is addition modulo two. A *cyclic run of ones* in a non-all-one circular bit string is a maximal consecutive block of ones between two zeros. The unique all-one domain-wall word is treated separately. The claim covers all ring lengths, including \(n=1,2\), and all nonnegative integer times.

## Proof

**1. Exact wall dynamics.** Set \(d_i=x_i\oplus x_{i+1}\). The majority rule changes the central bit exactly when both adjacent bits disagree with it, equivalently when \(d_{i-1}=d_i=1\). Hence
\[
(M_nx)_i=x_i\oplus(d_{i-1}d_i).
\]
Computing adjacent differences gives the autonomous wall rule
\[
\begin{aligned}
d'_i&=(M_nx)_i\oplus(M_nx)_{i+1}\\
&=d_i\oplus d_{i-1}d_i\oplus d_id_{i+1}\\
&=d_i(1\oplus d_{i-1}\oplus d_{i+1}).
\end{aligned}
\]
Thus a zero wall remains zero forever. A one wall survives precisely when its two neighboring walls are equal. If there is at least one zero wall, every maximal cyclic run of \(q\) ones evolves independently into a run of length \(q-2\) when \(q\ge2\); a run of length one persists; and a run of length two vanishes. In particular, the two endpoints disappear simultaneously for each run of length at least two.

After \(t\) iterations, a run initially of length \(q\) has stopped changing exactly when \(t\ge\lfloor q/2\rfloor\). If the wall word is already fixed, no adjacent walls equal one, so no majority-site changes occur. Conversely, whenever a wall run has length at least two, some site changes, so the configuration is not yet fixed. This proves the stated first-fixed-time formula.

**2. Alternating exception and maximal time.** A cyclic word \(d\) arises from some \(x\) if and only if \(\bigoplus_i d_i=0\), and then exactly two choices of \(x\) realize it, related by global bit complementation. Therefore the all-one wall word is admissible exactly when \(n\) is even. In that case its two preimages are the alternating configurations. Every bit flips on each synchronous update, yielding one two-cycle. No other state can lie on a nontrivial cycle, because its finite wall runs strictly shrink until fixed.

For a non-all-one wall word, \(q\le n-1\), and when the wall word has even weight, a single run may have length \(n-1\) if \(n\) is odd, or \(n-2\) if \(n\) is even and \(n\ge2\). These choices achieve \(\lfloor(n-1)/2\rfloor\). They also show the upper bound; for \(n=1\), both configurations are already fixed. This proves sharpness at all sizes.

**3. Exact weighted run enumerator.** Fix \(L\ge1\), let \(u\) mark each one wall, and define a transfer matrix \(T_L(u)\), indexed by \(0,1,\ldots,L\). From state \(j\), a zero goes to state zero with weight one; for \(j<L\), a one goes to state \(j+1\) with weight \(u\). No other transitions exist. A closed walk of length \(n\) has a uniquely determined cyclic bit label, and precisely the labeled cyclic binary words having at least one zero and all one-runs of length at most \(L\) are represented. Indeed, the current state is uniquely determined by the number of consecutive ones after the most recent zero. Consequently,
\[
\operatorname{tr}(T_L(u)^n)
=\sum_{\substack{d\in\{0,1\}^n,\ d\ne1^n\\
\text{every cyclic one-run has length}\ \le L}}u^{\sum_i d_i}.
\]

Let \(N\) be the weighted one-step forward shift \(j\to j+1\) (weight \(u\)), and let \({\bf1}e_0^{\mathsf T}\) describe all the zero edges. By the determinant lemma and nilpotence of \(N\),
\[
\begin{aligned}
\det(I-zT_L(u))
&=1-z\,e_0^{\mathsf T}(I-zN)^{-1}{\bf1}\\
&=1-z\sum_{j=0}^L(uz)^j=Q_L(u,z).
\end{aligned}
\]
For any finite square matrix over a commutative coefficient ring, the formal identity
\[
-z\frac d{dz}\log\det(I-zT)
=\sum_{n\ge1}\operatorname{tr}(T^n)z^n
\]
follows from \(\log\det(I-zT)=\operatorname{tr}\log(I-zT)\), or equivalently Newton identities. Therefore the weighted cyclic-run enumerator is the logarithmic derivative of \(Q_L\).

**4. Even-parity projection and cumulative counts.** By Step 1, the first-fixed time is at most \(t\) exactly when the wall word has at least one zero and every one-run has length \(q\le2t+1=L\). The parity constraint from Step 2 permits precisely the even-weight walls, with exactly two initial configurations per admissible wall word. For any weighted wall enumerator \(H(u)\), twice its even-weight contribution is \(H(1)+H(-1)\). Thus
\[
F_{n,t}=\operatorname{tr}(T_L(1)^n)+\operatorname{tr}(T_L(-1)^n).
\]
Inserting the determinant identity proves the displayed rational generating function. Taking differences gives the exact-time distribution, and the alternating exception has already been separated. Every argument holds at \(n=1,2\) because the cyclic wall parity and transfer-matrix descriptions remain valid. \(\square\)

For direct integer-coefficient evaluation, define \(c_{L,u}(0)=0\) and, for each \(n\ge1\),
\[
 c_{L,u}(n)=\sum_{k=1}^{\min(n-1,L+1)}u^{k-1}c_{L,u}(n-k)
 +\begin{cases}nu^{n-1},&n\le L+1,\\0,&n>L+1.\end{cases}
\]
It follows directly by multiplying \(-zQ'_L/Q_L\) by \(Q_L\) and comparing coefficients. The exact count is \(F_{n,t}=c_{2t+1,1}(n)+c_{2t+1,-1}(n)\). This recurrence requires only integer additions and gives a transparent way to reproduce arbitrary coefficients.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the formal logarithmic-derivative recurrence against independent finite transfer-matrix powers for \(1\le L\le8\), both parity weights, and lengths through fourteen. Separately, it exhaustively enumerates all binary starting configurations through length sixteen, independently applies the synchronous majority map, checks the predicted first-fixed time (or alternating two-cycle), verifies the sharp maximum, and checks every cumulative-count coefficient through the maximum possible finite hitting time. It prints `VERIFY_OK` on success.

For orientation, the respective counts of configurations first becoming fixed at times \(0,1,2,3\) are \((6,8,0,0)\) for \(n=4\), \((20,30,12,0)\) for \(n=6\), and \((46,144,48,16)\) for \(n=8\); each even ring also has precisely two alternating nonconverging configurations. These are finite checks, not substitutes for the all-length proof above.

## Relationship to prior work

The synchronous one-dimensional majority rule and its fixed points/two-cycles are classical. Tosic and Agha (2004), particularly Lemmas 3–4, identify the fixed configurations, alternating cycle, and remaining transients; those results cover the qualitative attractor partition but not the number of states with each prescribed first-fixed time. Inokuchi and Sato (2000) study limit cycles and transient lengths for finite threshold automata with fixed, rather than periodic, boundary conditions. Tosic (2016) enumerates stable (fixed) majority configurations; that addresses the \(t=0\) specialization of the present count, not the entire time-indexed distribution. Nakar and Ron (2022) analyze possible asymptotic periodic structures at general majority radius, not this exact finite-size/finite-time generating function.

The new assertion is specifically the **all-length hitting-time identity and rational generating family**, together with the sharp pointwise wall-run formula; it is not an originality claim for the majority rule, qualitative fixed-point classification, the elementary run-erasure mechanism, or the fixed-point count alone. Historical priority is qualified because a highly relevant early monograph by Goles and Martínez (1990) was not accessible in full for a conclusive comparison. The present account gives a complete self-contained proof rather than treating an unsuccessful literature search as proof of novelty.

## Limitations

The statements concern only one-dimensional radius-one synchronous binary majority with periodic spatial boundaries, not asynchronous updates, larger neighborhoods, stochastic rules, or arbitrary transient-to-cycle times. No claim about spatial entropy of unbounded-radius systems, inverse-image counts, or asymptotic probabilities under biased product measures is made. Earlier work may contain equivalent counting formulas under a different parameterization; the inaccessible historical source leaves a residual priority risk.

## References

1. E. Goles and S. Martínez, *Neural and Automata Networks: Dynamical Behavior and Applications*, Springer/Kluwer, 1990, chapter “Uniform One and two Dimensional Neural Networks,” pp. 97–136. https://doi.org/10.1007/978-94-009-0529-0_5 (chapter preview, not full text).
2. S. Inokuchi and T. Sato, “On Limit Cycles and Transient Lengths of Cellular Automata with Threshold Rules,” *Bulletin of Informatics and Cybernetics* 32 (2000), 23–60. https://doi.org/10.5109/13492 ; open text https://catalog.lib.kyushu-u.ac.jp/opac_download_md/13492/p023.pdf .
3. P. T. Tosic and G. A. Agha, “Characterizing Configuration Spaces of Simple Threshold Cellular Automata,” *ACRI* (2004). https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf .
4. P. Tosic, “On Enumerating Stable Configurations of Cellular Automata with the MAJORITY update rule,” public manuscript (2016). https://www.researchgate.net/publication/310515639_On_Enumerating_Stable_Configurations_of_Cellular_Automata_with_the_MAJORITY_update_rule .
5. Y. Nakar and D. Ron, “The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity,” preprint (2022). https://arxiv.org/abs/2205.08972 .
