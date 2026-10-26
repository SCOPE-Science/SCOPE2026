# Sharp twelve-cycle resonance and an eleven-step transient bound for tripartite excitation

## Finding

For all positive integers \(a,b,c\), let \(G=K_{a,b,c}\) be the simple complete tripartite graph, with labelled parts of sizes \(a,b,c\). At every synchronous step, a vertex in state \(1\) (excited) becomes \(2\) (refractory), a vertex in state \(2\) becomes \(0\) (resting), and a vertex in state \(0\) becomes \(1\) precisely when it has at least **two distinct** excited neighbours. Let \(F\) denote this map.

**Universal transient and orbit spectrum.** For every choice of sizes,
\[
 F^{23}=F^{11}.
\]
Thus every initial configuration becomes periodic within eleven steps, and every least orbit period belongs to \(\{1,3,4,12\}\). The bound eleven is sharp, even among tripartite graphs, as the displayed initial state on \(K_{5,2,3}\) in the verification section shows. The all-rest state is the only fixed point.

**Exact resonance threshold.** Set
\[
 B(n)=\begin{cases}\displaystyle\sum_{h=2}^{n-2}\binom nh=2^n-2n-2,&n\ge4,\\0,&1\le n<4,\end{cases}\qquad
 J(n)=\begin{cases}\displaystyle\frac{3!}{(3-n)!},&1\le n\le3,\\0,&n\ge4.\end{cases}
\]
The number \(R_{12}(a,b,c)\) of **labelled configurations of least period twelve**, not the number of orbits, is exactly
\[
 \boxed{R_{12}(a,b,c)=2\bigl[J(a)B(b)B(c)+J(b)B(a)B(c)+J(c)B(a)B(b)\bigr].}
\]
Consequently, twelve-cycles occur if and only if **exactly one** of the three part sizes belongs to \(\{1,2,3\}\) and the other two are at least four. The number of distinct twelve-cycles is \(R_{12}(a,b,c)/12\). For example, \(K_{4,4,1}\) has 216 least-period-twelve states, hence 18 distinct twelve-cycles, whereas \(K_{4,4,4}\) has none.

**Exact census of the other recurrent periods.** For \(p\in\{1,3,4,12\}\), define \(H_p(q)\in\{0,1\}\) by the explicit finite rules in the proof: start from the capped nine-entry occupancy vector \(q\), iterate the capped-profile map and each initially occupied vertex-state tag for \(p\) steps, and put \(H_p(q)=1\) if and only if the profile and all occupied tags return. For each part \(i\), let \(m_{i,0},m_{i,1},m_{i,2}\) be arbitrary nonnegative integers summing to its specified size \(n_i\), and set \(q_{i,s}=\min\{2,m_{i,s}\}\). Then
\[
 P_p=\sum_{\substack{m_{i,0}+m_{i,1}+m_{i,2}=n_i\\i=1,2,3}}
 \prod_{i=1}^3\binom{n_i}{m_{i,0},m_{i,1},m_{i,2}}\,H_p(q)
\]
counts the labelled configurations fixed by the \(p\)-fold update, with \((n_1,n_2,n_3)=(a,b,c)\). The exact least-period counts are \(R_1=P_1=1\), \(R_3=P_3-P_1\), \(R_4=P_4-P_1\), and \(R_{12}=P_{12}-P_3-P_4+P_1\). This is a fixed-size finite-state coefficient formula valid for arbitrary sizes, not a bound on small parameters.

## Assumptions and scope

Graphs are finite, undirected, simple, and complete between the three nonempty independent parts, with no edges within a part. Vertices are labelled, all updates are simultaneous, and the excitation threshold is exactly two distinct neighbours in state \(1\). All assertions are deterministic for every initial assignment from \(\{0,1,2\}^{a+b+c}\). No conclusion about general graphs, larger thresholds, asynchronous dynamics, or additional state colours is asserted.

## Proof

**1. Exact nine-coordinate quotient.** Write \(m_{i,s}(x)\) for the number of vertices in part \(i\) currently in state \(s\), and \(q_{i,s}=\min\{2,m_{i,s}\}\). Put
\[
 \varepsilon_i(q)=\mathbf1\!\left[\sum_{j\ne i}q_{j,1}\ge2\right].
\]
Every resting vertex in part \(i\) has the same excitation predicate, because it is adjacent to **all and only** vertices in the other two parts. Thus the exact capped update is
\[
 (q_{i,0}',q_{i,1}',q_{i,2}')=
 \bigl(\min\{2,q_{i,2}+(1-\varepsilon_i)q_{i,0}\},\ \varepsilon_iq_{i,0},\ q_{i,1}\bigr).
\]
Here truncation is exact because \(\min(2,u+v)=\min(2,\min(2,u)+\min(2,v))\) for nonnegative integers and because comparing an excited-neighbour count with two requires no larger counts. Hence this deterministic map on \(3^9=19{,}683\) profiles projects every labelled trajectory, regardless of part sizes.

**2. Tagged-vertex lift.** A tagged vertex in part \(i\) with current state \(s\) updates by \(1\mapsto2\), \(2\mapsto0\), \(0\mapsto\varepsilon_i(q)\). Appending the part index and tag state gives a deterministic graph with \(3^9\cdot3\cdot3=177{,}147\) states. Every original vertex trajectory is **exactly** a path in this finite graph driven by its common capped-profile trajectory. The complete integer enumeration in `verify.py`, using the displayed formulas rather than sampled graph sizes, establishes the pointwise identity \(T^{23}=T^{11}\) on all 177,147 tagged states. Applying it to every vertex proves \(F^{23}=F^{11}\) on every \(K_{a,b,c}\), hence all eventual periods divide twelve.

**3. Remove the spurious divisors.** For a capped profile \(q\), a labelled periodic state of period dividing \(p\) requires and is characterized by (i) return of \(q\) after \(p\) steps and (ii) return of every initially *occupied* tag \((i,s)\) after those steps; all vertices with that initial pair share the exact same tagged evolution. Thus \(H_p\) above is a necessary-and-sufficient test, and the multinomial sum follows by assigning the labelled vertices to phase populations. Exhaustive evaluation of every one of the 19,683 profiles proves \(H_2(q)\Rightarrow H_1(q)\) and \(H_6(q)\Rightarrow H_3(q)\). Therefore primitive periods two and six are absent. Only the all-rest assignment is fixed, since any vertex in state one or two changes at the next step.

**4. Classify the twelve-resonance profiles.** The same finite enumeration verifies that the full set of profiles satisfying \(H_{12}(q)=1\), \(H_3(q)=0\), and \(H_4(q)=0\) consists of **exactly 42** patterns, precisely as follows. After permuting the three parts, the capped phase populations are
\[
 (2,0,2),\qquad(2,2,0),\qquad(\delta_0,\delta_1,\delta_2),
 \quad \delta_s\in\{0,1\},\quad \delta_0+\delta_1+\delta_2\ge1.
\]
One may interchange the first two patterns. There are three choices of the small part, two orientations of the large patterns, and seven nonempty binary assignments to the small part: \(3\cdot2\cdot7=42\). This equality is checked as an **exact set equality** in `verify.py`; it is not inferred from experiments on selected graph sizes. For an actual graph, the two large parts each need at least two vertices of each of two designated states, contributing \(B(a)\) and \(B(b)\). The remaining part has exactly one vertex in each occupied state and therefore size \(c\in\{1,2,3\}\), contributing \(J(c)\) injections of its labelled vertices into the three states. Multiply by the two orientations and sum over the choice of small part to obtain the boxed formula and its if-and-only-if threshold.

**5. Sharpness.** On \(K_{5,2,3}\), assign the ordered state lists \((0,1,1,2,2)\), \((0,2)\), and \((0,1,1)\) to the three labelled parts. Direct application of the vertex-level update gives \(F^{22}(x)\ne F^{10}(x)\) and \(F^{23}(x)=F^{11}(x)\). Since every periodic state has period dividing twelve, the state at time ten is not yet periodic, whereas the state at time eleven is. Thus the uniform eleven-step bound cannot be lowered.

## Verification

`verify.py` is a standalone exact-integer verifier (Python 3, standard library only). It reconstructs the finite quotient, checks the universal tagged identity on all 177,147 states, tests the exclusions of periods two and six, and verifies the **whole** 42-profile description by set equality. It also independently updates the original labelled vertices for nine parameter triples, checking the allowed cycle periods, the exact twelve-state formula and the multinomial periodic-point census. The numerical verification output is retained in `verify_output.txt`. Finite enumeration here is a complete **proof of the finite quotient statements** because all its states are exhaustively covered, not an extrapolation from a finite sample of graph sizes. The quotient lemma transports these exact finite checks to arbitrarily large part sizes.

## Relationship to prior work

Fisch, Gravner and Griffeath (1991; public preprint 1993) established the threshold-dependent Greenberg–Hastings framework and investigated excitation waves on two-dimensional lattices, not the finite complete-tripartite orbit census. Durrett and Griffeath (1993) studied stable periodic structures and threshold-range behaviour on lattices. Gravner, Lyu and Sivakoff (2016 preprint; 2018 publication) investigate three-colour excitable media on arbitrary graphs with the **one-neighbour** excitation rule; its comparison theorem does not apply at threshold two. Existing bipartite threshold-two classifications describe three- and four-cycles but do not imply the twelve-cycle resonance after coupling to a third nonempty part. The precise mechanism here is the coexistence of a four-step alternating excitation core and a three-step spectator orbit, possible only when the spectator part has at most three vertices.

## Limitations

The theorem is restricted to three nonempty graph parts, three states and threshold two. The finite quotient is small only because the number of parts and threshold are fixed. The standalone certificate is computationally exhaustive and transparent but has not undergone independent mathematical or software audit. The originality search was bounded to accessible indexed records and inspected primary text; an unindexed equivalent cannot be excluded. The 1993 Durrett–Griffeath full text could not be retrieved through the attempted open route; its abstract and bibliographic scope alone are not used to assert a whole-document noncoverage claim.

## References

1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39; accessible full text: https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf ; preprint arXiv:patt-sol/9304001 (first dated posting 1993-04-02).
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics **2** (1993), 183–208; arXiv:patt-sol/9303002 (dated 1993-03-22).
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, Annals of Applied Probability **28** (2018), 3324–3357; arXiv:1610.07320 (dated 2016-10-24), full text https://arxiv.org/pdf/1610.07320 .
4. S. Spence Adams, Z. Brass, C. Stokes and D. Sakai Troxell, *Irreversible k-threshold and majority conversion processes on complete multipartite graphs and graph products*, arXiv:1102.5361 (2011-02-25), an irreversible two-state model distinct from refractory excitation.
