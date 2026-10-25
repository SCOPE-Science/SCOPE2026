# A two-index ordering law for serial saturating nutrient-removal reaches

## Finding

A succession of saturable removal reaches need not have one best upstream-to-downstream order for every incoming nutrient concentration. For the precise discrete model below, however, two parameter indices give a complete answer to the question of whether such a universally optimal ordering exists. For every finite family of reaches with pairwise distinct half-saturation constants, the globally least-exporting order at all sufficiently small positive inputs is by **decreasing residual index** \(K_i-u_i\), with ties settled by decreasing \(K_i\); at all sufficiently large inputs it is by decreasing \(K_i\). A single order is optimal at *every* positive input if and only if these two rankings coincide, equivalently

\[
K_i>K_j\quad\Longrightarrow\quad K_i-u_i\ge K_j-u_j
\quad\text{for every pair }i,j.
\]

Under this criterion, decreasing \(K_i\) is the unique globally optimal order at every positive input. If the criterion fails, no fixed ordering is optimal for every input. For two reaches with \(K>L\), the preference reverses exactly once if and only if \(K-u<L-v\), and its unique positive switching concentration is an explicit quadratic root.

## Assumptions and scope

For each of \(n\ge2\) distinct serial units, specify a half-saturation concentration \(K_i>0\) and a concentration-scale removal capacity \(u_i\) with \(0<u_i<K_i\). An input concentration \(x>0\) leaves unit \(i\) as

\[
T_i(x)=x-\frac{u_ix}{K_i+x}
=\frac{x(K_i-u_i+x)}{K_i+x}.
\]

This is an algebraic **finite-step**, constant-flow, no-intermediate-source removal model: it is not the exact continuous plug-flow solution of a Michaelis--Menten differential equation. The condition \(u_i<K_i\) ensures positivity and increasing input-output response. The same unit is used once; there are no dilution, intermediate nutrient additions, transport delays, or external state variables. A permutation \(\pi=(\pi_1,\ldots,\pi_n)\) gives outlet concentration \(T_{\pi_n}\circ\cdots\circ T_{\pi_1}(x)\), to be minimized. For the family-wide ordering theorem, the values \(K_i\) are pairwise distinct. Ties in \(K_i-u_i\) are permitted.

## Proof

**1. Monotone stages.** For every admissible unit and every \(x>0\),

\[
0<T_i(x)<x,\qquad
T_i'(x)=1-\frac{u_iK_i}{(K_i+x)^2}>1-\frac{u_i}{K_i}>0.
\]

Consequently, a strict two-stage improvement remains strict after any fixed downstream chain of units. Every upstream intermediate concentration is in \((0,x]\) and exceeds \(x-\sum_i u_i\).

**2. Exact two-stage commutator.** Let the parameters of units \(i,j\) be \((K,u)\), \((L,v)\). Put

\[
\begin{aligned}
P(x)={}&(K-L)x^2+\bigl[(K-L)(K+L)-Ku+Lv\bigr]x\\
&+KL(K-L-u+v),\\
D(x)={}&(K+x)(L+x)
\bigl[(K+x)(L+x)-ux\bigr]
\bigl[(K+x)(L+x)-vx\bigr].
\end{aligned}
\]

Direct expansion, with all denominators positive, gives

\[
T_j(T_i(x))-T_i(T_j(x))
=-\frac{uvx^2P(x)}{D(x)}.
\tag{1}
\]

Thus unit \(i\) first yields less outlet nutrient if and only if \(P(x)>0\).

**3. Sharp two-unit classification.** Assume \(K>L\), and set the residual indices \(r_i=K-u\), \(r_j=L-v\). If \(r_i\ge r_j\), then \(u\le K-L+v\), so the coefficient of \(x\) in \(P\) obeys

\[
(K-L)(K+L)-Ku+Lv\ge (K-L)(L-v)>0.
\]

The constant term is nonnegative and the leading coefficient is positive; hence \(P(x)>0\) for all \(x>0\). This also handles the equality boundary \(r_i=r_j\).

If \(r_i<r_j\), then the constant term of \(P\) is negative while the quadratic coefficient is positive. Its two real roots have opposite signs, so exactly one, \(x_*\), is positive. Writing \(A=K-L>0\), \(B=(K-L)(K+L)-Ku+Lv\), and \(C=KL(K-L-u+v)<0\), we have

\[
x_* =\frac{-B+\sqrt{B^2-4AC}}{2A}.
\]

For \(0<x<x_*\), \(P(x)<0\), so \(j\) upstream is strictly better; for \(x>x_*\), \(i\) upstream is strictly better; and only at \(x=x_*\) are their outlets equal. Reversing the names gives the case \(K<L\). In the excluded equal-\(K\) pair case, \(P(x)=K(v-u)(x+K)\), so no positive switching point occurs unless the stages are identical.

**4. All-concentration ordering.** Suppose \(K_i>K_j\) implies \(K_i-u_i\ge K_j-u_j\) for every pair. By step 3, placing the larger-\(K\) unit first strictly improves any inverted adjacent pair at every positive intermediate input. Since all downstream maps are strictly increasing, repeated adjacent exchanges show that decreasing \(K_i\) uniquely minimizes the final outlet, for every \(x>0\).

For an arbitrary family, every unordered pair has, by step 3, either a fixed preference or a single positive switch. As input approaches zero, the preferred order of a pair is decreasing \(r_i=K_i-u_i\); for equal residual indices it is decreasing \(K_i\). Since the family is finite, choose \(\varepsilon>0\) below every positive pair-switch concentration (and choose any \(\varepsilon>0\) if there are none). At \(0<x<\varepsilon\), all intermediate concentrations lie in \((0,x]\). Every adjacent exchange violating the lexicographic descending order \((r_i,K_i)\) is therefore strictly improving. The resulting order is uniquely globally optimal.

For large input, let \(M\ge0\) exceed every positive pair-switch concentration (take \(M=0\) if there are none) and let \(U=\sum_i u_i\). Whenever \(x>M+U\), every intermediate input is greater than \(M\), and step 3 makes decreasing \(K_i\) the strict preferred order for every adjacent pair. Repeated exchanges again yield a unique global optimum. If any pair has \(K_i>K_j\) but \(r_i<r_j\), the small- and large-input unique optimizing permutations differ. Therefore no fixed permutation minimizes outlet concentration for every \(x>0\), completing the iff statement.

## Verification

The exact symbolic commutator identity and explicit rational example were checked with a standalone SymPy/Fraction program in `verification/check_serial_uptake.py`. It also tested 10,000 seeded random admissible pairs and 133 complete rational-arithmetic permutation censuses for families of two through five stages at verified small and large inputs. The finite tests are consistency checks, not a proof for all real parameters; the universal assertions follow from the preceding algebra and interchange argument.

For the concrete two-unit example

\[
(K,u)=(2,7/4),\qquad(L,v)=(1,1/3),
\]

the exact polynomial is \(P(x)=(x-1)(x+5/6)\). The preferred upstream unit is \(L=1\) for \(0<x<1\) and \(K=2\) for \(x>1\). Both orders give exactly \(65/204\) at \(x=1\). At \(x=1/2\) the lower-\(K\)-first output is \(161/1548\), below the higher-\(K\)-first output \(49/460\); at \(x=2\) the higher-\(K\)-first output is \(129/136\), below \(146/153\).

For a three-unit contrast, choose \((K_i,u_i)=(3,29/10),(2,3/2),(1,1/10)\). At input \(x=1/100\), the unique best sequence of \(K\)-values is \((1,2,3)\); at input \(x=10\), it is \((3,2,1)\). Every one of the six orderings was compared in exact rational arithmetic.

## Relationship to prior work

Covino, McGlynn and Baker (2010) measured spatially differing saturable nutrient uptake and explicitly highlighted stream-reach arrangement as relevant to downstream export. Their full accessible article discusses physical and biological retention, observed Michaelis--Menten uptake curves, and arrangement at the network level, but does not present this finite-step two-index universal-order iff theorem or the exact two-unit switching criterion. Ensign and Doyle (2006) synthesize nutrient spiraling across networks and study stream-order scaling, not optimization over permutations of saturable removal maps. Basu and colleagues (2011) analyze spatial/temporal averaging of first-order effective removal rates; they do not supply the claimed algebraic permutation result in the portions inspected. These are distinct problems and do not imply the theorem without an additional interchange analysis.

Sakamoto (1994) treats transfer functions for consecutive Michaelis--Menten-type reactions near steady state. The accessible abstract describes a different, dynamic input-output approximation, not this finite-step nutrient-removal composition, but its full text was unavailable for inspection. More general results on ordering monotone rational maps may imply this result, and literature searches cannot establish uniqueness of priority. The Michaelis--Menten functional form, serial processing and adjacent-interchange proof method are established; only the precise combined classification is advanced as a candidate contribution.

## Limitations

The result is exact only for the specified one-pass finite-step algebraic model, with \(0<u_i<K_i\), one use per stage, constant flow, no additions or mixing, and common substrate. It is not an observed best arrangement for a physical river and is not a theorem for continuous plug-flow, time-dependent microbial dynamics, dispersion, or network branching. The low/high sorting theorem is an existence statement for sufficiently extreme inputs; it does not classify the intermediate best permutation or the number of switches of that global permutation. No empirical parameter uncertainty, environmental intervention costs, or feasibility constraints are included. Historical originality remains provisional because relevant earlier full texts and general rearrangement theory may cover the statement.

## References

1. T. Covino, B. McGlynn, M. Baker, “Separating physical and biological nutrient retention and quantifying uptake kinetics from ambient to saturation in successive mountain stream reaches,” *Journal of Geophysical Research: Biogeosciences* 115 (2010), G04010, doi:10.1029/2009JG001263 (first publicly published 2010-10-08).
2. S. H. Ensign and M. W. Doyle, “Nutrient spiraling in streams and river networks,” *Journal of Geophysical Research: Biogeosciences* 111 (2006), G04009, doi:10.1029/2005JG000114.
3. N. B. Basu et al., “Spatiotemporal averaging of in-stream solute removal dynamics,” *Water Resources Research* 47 (2011), W00J06, doi:10.1029/2010WR010196.
4. N. Sakamoto, “A transfer-function representation for the input-output relation in consecutive Michaelis-Menten-type reactions,” *BioSystems* 33 (1994), 99–110, doi:10.1016/0303-2647(94)90050-7.
