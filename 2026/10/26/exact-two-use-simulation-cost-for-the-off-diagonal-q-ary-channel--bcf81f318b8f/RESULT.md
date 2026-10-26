# Exact Two-Use Simulation Cost for the Off-Diagonal \(q\)-Ary Channel

## Finding

For \(q\ge2\), let \(W_q(y\mid x)=1/(q-1)\) when \(y\ne x\) and zero otherwise on \([q]\). In the common-randomness-assisted, fixed-codebook, worst-case total-variation model, the exact minimum codebook size for two independent uses is \(M_0^\star(W_q^{\otimes2})=4\) for \(q=2\) and \(M_0^\star(W_q^{\otimes2})=3\) for every \(q\ge3\).

Let \(q\ge2\), let \([q]=\{0,1,\ldots,q-1\}\), and define the channel

\[
W_q(y\mid x)=\begin{cases}1/(q-1),&y\ne x,\\0,&y=x.\end{cases}
\]

For the common-randomness-assisted simulation model with a fixed message alphabet of size \(M\), worst-case total-variation error zero, and two independent uses of this channel, the exact minimum is

\[
M_0^\star(W_q^{\otimes2})=\begin{cases}4,&q=2,\\3,&q\ge3.\end{cases}
\]

Thus the exact cost is three messages for every alphabet size at least three, independent of \(q\), while the binary endpoint requires four.

## Assumptions and scope

The input and output alphabets are both \([q]^2\). Given input \(x=(x_1,x_2)\), the target output is uniform on

\[
N(x)=\{y=(y_1,y_2)\in[q]^2:y_1\ne x_1,\;y_2\ne x_2\},
\]

which has \((q-1)^2\) elements. The simulator has unlimited shared randomness independent of the input; the sender transmits one of \(M\) indices and the receiver's output is determined by that index and the shared randomness. All random choices can be included in the shared randomness, so it is enough to consider deterministic encoder and decoder maps conditioned on the shared seed. Error is the supremum, over all inputs, of total-variation distance. This is an exact-simulation statement: no positive error tolerance is allowed. It makes no claim for blocklengths other than two or for approximate error.

## Proof

For a fixed shared seed \(u\), let \(C_u\subseteq[q]^2\) be the set of outputs the decoder can produce from the \(M\) message indices. Then \(|C_u|\le M\). Exact simulation requires the output to lie in \(N(x)\) with probability one for each input \(x\). Consequently, for almost every seed, \(C_u\cap N(x)\ne\emptyset\) for every \(x\). Since the relation is symmetric, \(x\in N(y)\) exactly when \(y\in N(x)\); therefore the sets \(N(y)\), for \(y\in C_u\), must cover all \(q^2\) possible inputs.

For \(q\ge3\), three outputs suffice. Fix three distinct symbols \(a,b,c\) and start with \(C_0=\{(a,a),(b,b),(c,c)\}\). For any input \(x=(x_1,x_2)\), at most two of \(a,b,c\) can equal one of \(x_1,x_2\), so at least one diagonal pair differs from \(x\) in both coordinates. Randomize this construction by choosing independent uniform injections \(\pi_1,\pi_2:\{a,b,c\}\to[q]\) and using

\[
C_U=\{(\pi_1(t),\pi_2(t)):t\in\{a,b,c\}\}.
\]

Every realized codebook has three distinct outputs and intersects \(N(x)\) for every input. The encoder chooses uniformly among its valid indices. This choice is implementable using a shared uniform tie-breaker \(V\in\{0,1,2,3,4,5\}\): if there are \(k\in\{1,2,3\}\) valid indices, choose the \(V\bmod k\)-th valid index in a fixed ordering. Since each such \(k\) divides six, this is uniform. The random construction and selection rule are equivariant under independent permutations of the two alphabet coordinates. The subgroup fixing \(x\) acts transitively on \(N(x)\); hence the simulated output law is constant on \(N(x)\). It is supported there and has total mass one, so it is exactly uniform on \(N(x)\). Thus \(M_0^\star\le3\).

For the lower bound, a single output \(y\) is compatible with exactly \((q-1)^2\) inputs, namely the elements of \(N(y)\). For two outputs \(y,z\), let \(d\in\{0,1,2\}\) be their Hamming distance. Coordinatewise counting gives

\[
|N(y)\cap N(z)|=(q-1)^{2-d}(q-2)^d.
\]

This intersection is smallest when \(d=2\). Hence

\[
|N(y)\cup N(z)|\le2(q-1)^2-(q-2)^2=q^2-2<q^2.
\]

Two outputs cannot cover all inputs. The almost-sure covering requirement therefore forces \(M\ge3\) for \(q\ge3\), proving equality.

When \(q=2\), each \(N(x)\) is a singleton, containing only the coordinatewise complement of \(x\). Exact simulation requires each of the four possible outputs to be available for its corresponding input with probability one. Thus every shared seed must allow all four outputs, so \(M\ge4\); the four-output codebook attains this bound.

## Verification

The proof uses two exact ingredients: (i) the support-covering necessity forced by zero total-variation error and deterministic decoding conditional on shared randomness; and (ii) the exact intersection count for two neighborhoods. The upper construction has at least one valid index for every input because two coordinate-equality constraints exclude at most two of three indices. For the lower bound, the cases \(d=0,1,2\) are all covered by the displayed intersection formula, and the largest two-neighborhood union is \(q^2-2\). The binary case is handled separately because its target support is a singleton. No finite experiment is used as proof, and no asymptotic conclusion is inferred.

## Relationship to prior work

Lungu, Wagner, and Kontoyiannis study worst-case total-variation channel simulation and third-order asymptotics for symmetric channels, but their main expansion assumes fixed tolerance \(0<\epsilon<1\) and positive channel dispersion. The present claim is an exact finite-block result at zero simulation error for a zero-dispersion channel, so that expansion does not imply it. Cao, Ramakrishnan, Berta, and Tomamichel give the common-randomness simulation model and explicitly discuss the ternary channel whose output is uniform over symbols different from the input; their treatment does not state the exact two-use codebook optimum proved here. Sriramu and Wagner study exact synthesis under an i.i.d. input distribution with average prefix-free communication length, a different objective from fixed-size worst-case simulation.

## Limitations

The result concerns only two uses of the fully off-diagonal channel and exact simulation. It does not determine the optimum for three or more uses, for positive error tolerance, or for other support patterns. Exact-formulation searches and primary-text comparisons found no direct statement of this exact two-use optimum, but unsuccessful searches cannot establish global novelty. A general support-covering theorem in an uninspected source could subsume this small case; this remains a residual literature risk.

## References

1. Valentinian Lungu, Aaron B. Wagner, and Ioannis Kontoyiannis, “Fine asymptotics for approximate simulation of symmetric channels,” arXiv:2610.15877, submitted 2026-10-11. Full text inspected for its simulation model, channel-symmetry definitions, positive-dispersion assumption, and main theorem.
2. Michael X. Cao, Navneeth Ramakrishnan, Mario Berta, and Marco Tomamichel, “Channel Simulation: Finite Blocklengths and Broadcast Channels,” arXiv:2212.11666; IEEE Transactions on Information Theory 70(10), 2024. Full text inspected for the common-randomness worst-case model and its ternary off-diagonal channel example.
3. Sharang M. Sriramu and Aaron B. Wagner, “Optimal Redundancy in Exact Channel Synthesis,” arXiv:2401.16707, 2024. Full text inspected; its i.i.d.-source, average prefix-free-length objective is distinguished from the fixed-codebook worst-case model here.
