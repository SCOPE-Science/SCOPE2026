# Strict fidelity ordering and a factor-two star advantage for noisy complete-bipartite graph states

## Finding

Let \(n\ge4\), \(1\le a\le b\), \(a+b=n\), and let \(\lvert K_{a,b}\rangle\) denote the qubit graph state of the complete bipartite graph with parts of sizes \(a\) and \(b\). Independently apply the single-qubit channel \(\mathcal D_q(\rho)=(1-q)\rho+qI/2\), \(0\le q\le1\), after preparing the ideal graph state. Define its overlap fidelity
\[
 F_{a,b}(q)=\langle K_{a,b}\rvert\mathcal D_q^{\otimes n} (\lvert K_{a,b}\rangle\langle K_{a,b}\rvert)\lvert K_{a,b}\rangle.
\]
For \(r=1-q\), \(t=(1+r)/2\), \(u=(1-r)/2\), \(E_k=t^k+u^k\), and \(O_k=t^k-u^k\), the exact formula is
\[
 F_{a,b}(q)=\frac14\bigl(E_aE_b+r^bO_a+r^aO_b+r^{a+b}\bigr).
\]
For every \(q\in(0,1)\) and every \(1\le a<\lfloor n/2\rfloor\),
\[
 F_{a,n-a}(q)>F_{a+1,n-a-1}(q).
\]
Therefore stars \(K_{1,n-1}\) uniquely maximize the fidelity and the most balanced bicliques \(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\) uniquely minimize it within this graph family, modulo graph isomorphism. For every fixed \(q\in(0,1)\),
\[
 \lim_{n\to\infty}\frac{F_{1,n-1}(q)}{F_{\lfloor n/2\rfloor,\lceil n/2\rceil}(q)}=2.
\]
More generally, if \(a\ge1\) stays fixed and \(n\to\infty\), the same ratio with \(F_{a,n-a}(q)\) in the numerator tends to \(1+(u/t)^a+(r/t)^a\). The endpoint values are \(F_{a,b}(0)=1\) and \(F_{a,b}(1)=2^{-n}\), independently of \(a,b\).

## Assumptions and scope

The graph is simple, complete bipartite, and has at least four qubits; both parts are nonempty. The ideal graph state is obtained by applying controlled-\(Z\) gates on all cross-part edges to \(\lvert+\rangle^{\otimes n}\). Noise acts only after preparation and is independent, isotropic, and identical at every vertex. Fidelity here means overlap with the original pure state; no entanglement monotone or circuit-generation yield is inferred. The paper of Numajiri et al. uses a Pauli-error probability \(p\), related to this channel convention by \(q=4p/3\) on the common physical parameter range.

## Proof

**Exact stabilizer calculation.** Label the two parts \(A,B\), and take the canonical stabilizer generators \(K_v=X_v\prod_{w\sim v}Z_w\). For generator selections \(I\subseteq A\) and \(J\subseteq B\), write \(i=\lvert I\rvert\), \(j=\lvert J\rvert\). The support weight of \(\prod_{v\in I\cup J}K_v\), ignoring its harmless overall sign, equals the sum of the following two contributions: on \(A\), the contribution is \(i\) if \(j\) is even and \(a\) if \(j\) is odd; on \(B\), the contribution is \(j\) if \(i\) is even and \(b\) if \(i\) is odd. This remains true for overlapping local \(X\) and \(Z\), which give nonidentity \(Y\) operators. By the independent depolarizing channel, any Pauli operator of weight \(w\) has expectation multiplied by \(r^w\). Expanding the graph-state projector as the mean of its \(2^n\) stabilizers, the fidelity is \(2^{-n}\) times the sum of \(r^w\) over all \(I,J\).

The binomial even and odd sums satisfy
\[
 \sum_{i\ \mathrm{even}}\binom ai r^i=2^{a-1}E_a,
 \qquad \sum_{i\ \mathrm{odd}}\binom ai r^i=2^{a-1}O_a.
\]
The four parity choices for \(i,j\) respectively contribute \(E_aE_b/4\), \(r^bO_a/4\), \(r^aO_b/4\), and \(r^{a+b}/4\). This proves the exact formula for all stated sizes and endpoint noise strengths.

**Strict partition ordering.** Assume \(0<q<1\). Put \(x=u/t\), \(y=r/t\); then \(x,y\in(0,1)\) and \(x+y=1\). Algebra gives
\[
 \frac{4F_{a,b}}{t^n}=1+x^n+y^n+H(a,b),
\]
where
\[
 H(a,b)=x^a+x^b+y^a+y^b-x^ay^b-y^ax^b.
\]
For one balancing step \(b\ge a+2\), let \(m=b-a-1\ge1\). Direct subtraction yields the exact identity
\[
\begin{aligned}
 H(a,b)-H(a+1,b-1)
 &=yx^a(1-x^m)+xy^a(1-y^m)\\
 &\quad -(y-x)(xy)^a(y^m-x^m).
\end{aligned}
\]
The first two terms are strictly positive. If \(y>x\), the term subtracted on the second line is positive but strictly smaller than the *first* term, because
\[
 \frac{(y-x)(xy)^a(y^m-x^m)}{yx^a(1-x^m)}
 =\frac{y-x}{y}\,y^a\,\frac{y^m-x^m}{1-x^m}<1.
\]
Here each factor is in \((0,1)\). If \(x>y\), both factors \(y-x\) and \(y^m-x^m\) are negative, so the subtracted term is again positive, but its ratio to the *second* positive term is
\[
 \frac{(x-y)(xy)^a(x^m-y^m)}{xy^a(1-y^m)}
 =\frac{x-y}{x}\,x^a\,\frac{x^m-y^m}{1-y^m}<1.
\]
If \(x=y\), the subtracted term vanishes. In all three cases the difference is strictly positive. Repeated balancing proves the entire ordering and identifies the unique extrema up to interchanging parts.

**Sharp fixed-noise asymptotics.** Since \(0<r,u<t<1\), the normalized formula above implies
\[
 \frac{4F_{a,n-a}}{t^n}\longrightarrow1+x^a+y^a
 \quad\text{for fixed }a,
\qquad
 \frac{4F_{\lfloor n/2\rfloor,\lceil n/2\rceil}}{t^n}\longrightarrow1.
\]
The claimed ratio follows. When \(a=1\), \(x+y=1\), giving exactly \(2\). At \(q=0,1\), direct substitution into the closed formula gives the stated graph-independent values.

## Verification

Run `python3 verify.py` using the standard Python library. The verifier constructs every graph stabilizer independently by XORing explicit adjacency-neighbor masks, computes its Pauli support, and sums the exact rational expectations. It compares these direct sums with the closed formula for all part sizes at total orders \(2\) through \(11\), for five rational noise strengths. It additionally checks the strict inequalities for orders \(4\) through \(59\), the previously known star formula for orders \(2\) through \(29\), the large-order ratio at several rational strengths, and \(F_{1,3}(1/2)=49/256>45/256=F_{2,2}(1/2)\). The deterministic verifier returns `VERIFY_OK 3612`. These are finite consistency checks; the preceding algebra proves the all-size results.

## Relationship to prior work

The general graph-state stabilizer-fidelity identity is established in Tanizawa et al., *Physical Review Research* **5**, 043260 (2023), and in Numajiri et al., arXiv:2510.00548 (initial public version 1 October 2025), which also analyzes regular graph geometries and an exact fully connected graph-state formula. The complete-graph state is locally Clifford-equivalent to the star graph state, so the \(a=1\) formula \(F_{1,n-1}=[t^n+u^n+r^n]/2\) is not claimed as new. The derivation above extends the exact expression to every biclique split and proves a sharp strict ordering between all nonisomorphic splits, as well as the factor-two large-order comparison. Sen, Goodenough and Towsley, *Quantum* **9**, 1911 (2025), study noisily **generating and distributing** balanced complete-bipartite graph states via imperfect gates; their operation-by-operation noise model differs from one application of IID depolarization after ideal preparation and does not establish the ordering here. A broader previous exact specialization or implicit weight-enumerator inequality cannot be ruled out.

## Limitations

Only complete-bipartite graph states, not all connected graph states, are ranked. Fidelity is not an entanglement threshold, verification sample complexity, or fault-tolerance figure of merit; the fidelity-maximizing star might not maximize these other resources. The noise strength is fixed strictly inside \((0,1)\) for strict order and asymptotic ratios. The convergence is not uniform as noise tends to either endpoint with growing system size. Different noise channels, correlated noise, noise during controlled-\(Z\) preparation, and hardware-specific gate errors are outside scope. Independent scientific validation has not been performed.

## References

1. T. Numajiri, S. Yamashika, T. Tanizawa, R. Yoshii, Y. Takeuchi, and S. Tsuchiya, *Phase Transitions and Noise Robustness of Quantum Graph States*, arXiv:2510.00548 (first publicly posted 2025-10-01; later published in *Quantum* **10**, 2094 (2026)). See Secs. 2, 6.4, and Appendix B.
2. T. Tanizawa, Y. Takeuchi, S. Yamashika, R. Yoshii, and S. Tsuchiya, *Fidelity-estimation method for graph states with depolarizing noise*, *Physical Review Research* **5**, 043260 (2023), doi:10.1103/PhysRevResearch.5.043260.
3. A. Sen, K. Goodenough, and D. Towsley, *Multipartite Entanglement Distribution in Quantum Networks using Subgraph Complementations*, *Quantum* **9**, 1911 (2025); see Sec. 7.2 and its distinct imperfect-gate noise setting.
