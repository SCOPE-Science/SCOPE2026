# The all-zero word is the unique modal output of Rule 22 on every binary ring

## Finding
For every indexed cyclic binary ring of length \(n\ge3\), consider one synchronous update under elementary cellular automaton Rule 22, also called the *Exactly 1* rule. The all-zero output has strictly more predecessors than any other possible output. Its exact number of predecessors is
\[
P_n(0^n)=1+t_n,
\quad t_0=3,\ t_1=t_2=1,\quad
 t_n=t_{n-1}+t_{n-3}\quad(n\ge3).
\]
For every nonzero output \(y\) there is the uniform upper bound \(P_n(y)\le u_n<t_n\), where \(u_3=u_4=3\), \(u_5=4\), and \(u_n=u_{n-1}+u_{n-3}\) for \(n\ge6\). Thus uniqueness is strict at every length, not only asymptotically.

## Assumptions and scope
The sites are **indexed** as \(0,\ldots,n-1\), with subscripts modulo \(n\); rotations are different words unless their coordinate vectors coincide. For \(x\in\{0,1\}^n\), the update \(F_n(x)\) satisfies \((F_n(x))_i=1\) precisely if \(x_{i-1}+x_i+x_{i+1}=1\) in the ordinary integers. For an indexed output word \(y\), define its one-step fiber size as \(P_n(y)=|\{x:F_n(x)=y\}|\). The theorem ranges over all \(n\ge3\) and all binary outputs \(y\), including unreachable ones.

## Proof
**1. Cyclic transfer matrices.** Label pair states \(00,01,10,11\) in this order. Define the nonnegative matrices
\[
A_0=\begin{pmatrix}
1&0&0&0\\0&0&0&1\\0&1&0&0\\0&0&1&1
\end{pmatrix},\qquad
A_1=\begin{pmatrix}
0&1&0&0\\0&0&1&0\\1&0&0&0\\0&0&0&0
\end{pmatrix}.
\]
An entry records the allowable shift from pair \((x_{i-1},x_i)\) to pair \((x_i,x_{i+1})\) with prescribed Rule-22 output at index \(i\). A closed length-\(n\) path is in one-to-one correspondence with an indexed input \(x\); even for periodic input with a smaller least period, the starting pair is fixed by site zero. Consequently
\[
P_n(y)=\operatorname{tr}(A_{y_0}A_{y_1}\cdots A_{y_{n-1}}).
\]
The trace is invariant under a cyclic permutation of factors, so when \(y\ne0^n\) we may take its final symbol to be \(1\), and write the product as \(QA_1\), where \(Q\) contains the other \(n-1\) factors.

**2. Uniform envelope for nonzero outputs.** For a row vector \(v\ge0\), let \(\mathcal M(v)\) be the coordinatewise maximum of \(vA_0\) and \(vA_1\). For each of the four unit row vectors \(e_i\), set \(E_{i,0}=e_i\) and \(E_{i,m+1}=\mathcal M(E_{i,m})\). Monotonicity of right multiplication by the nonnegative matrices gives
\[
e_iA_{b_1}\cdots A_{b_m}\le E_{i,m}\quad\text{componentwise}
\]
for **every** binary product \((b_1,\ldots,b_m)\), by induction on \(m\). Direct multiplication gives \(E_{i,2}=(1,1,1,1)\) independently of \(i\). For every \(m\ge2\), the four envelopes remain equal to a row of the form \((a_m,a_m,b_m,c_m)\), with \(0\le a_m\le b_m\le c_m\). Indeed
\[
(a,a,b,c)A_0=(a,b,c,a+c),\quad
(a,a,b,c)A_1=(b,a,a,0),
\]
so their coordinatewise maximum is \((b,b,c,a+c)\). The inequality \(c\le a+c\) and \(b\le c\) preserve the ordering. Thus the triple satisfies the exact update \((a,b,c)\mapsto(b,c,a+c)\), initially \((1,1,1)\) at \(m=2\).

The only three nonzero diagonal contributions to \(\operatorname{tr}(QA_1)\) are \(Q_{0,2}\), \(Q_{1,0}\), and \(Q_{2,1}\). They are bounded respectively by \(b_{n-1}\), \(a_{n-1}\), and \(a_{n-1}\), and therefore
\[
P_n(y)\le 2a_{n-1}+b_{n-1}=:u_n.
\]
The triple update has characteristic polynomial \(\lambda^3-\lambda^2-1\), hence every component and its fixed linear combinations obey the recurrence \(u_n=u_{n-1}+u_{n-3}\). Direct evaluation gives \(u_3=u_4=3\) and \(u_5=4\).

**3. Exact all-zero fiber.** The matrix \(A_0\) is block diagonal after the isolated pair state \(00\): this gives one constant-zero predecessor and a three-state block
\[
B=\begin{pmatrix}0&0&1\\1&0&0\\0&1&1\end{pmatrix}.
\]
Thus \(P_n(0^n)=1+\operatorname{tr}(B^n)\). Direct multiplication proves \(B^3=B^2+I\), so with \(t_n=\operatorname{tr}(B^n)\) we obtain \(t_0=3,t_1=t_2=1\) and \(t_n=t_{n-1}+t_{n-3}\) for \(n\ge3\).

**4. Strictness.** The differences \(d_n=t_n-u_n\) obey the same order-three recurrence for \(n\ge6\). Their first three relevant terms are \(d_3=1,d_4=2,d_5=2\). Hence \(d_n>0\) for all \(n\ge3\). Consequently
\[
P_n(y)\le u_n<t_n<P_n(0^n)=1+t_n
\qquad (y\ne0^n),
\]
which proves the strict global maximum and its uniqueness. No asymptotics or finite enumeration enter this proof.

## Verification
Run `python3 verify.py` to independently check the transfer identity on every output through length eleven, the complete fiber mode by direct input enumeration through length sixteen, the exact envelope through fifty factors and recurrence identities through length one hundred. It prints `VERIFY_OK`. Separately compile `crosscheck.cpp` with a C++17 compiler and run it: this computes the image of every indexed input on rings of lengths three through twenty-two by bitwise arithmetic, checks that the all-zero fiber equals \(1+t_n\), and verifies uniqueness. It prints `CROSSCHECK_OK`. These are reproducibility checks; the complete proof is the induction and trace argument above.

For illustration, the exact maximum fiber sizes for \(n=3,4,\ldots,12\) are respectively \(5,6,7,11,16,22,32,47,68,99\). With uniform random input, the unique most probable output is always zero and has probability \((1+t_n)/2^n\).

## Relationship to prior work
Jen (1989, especially Sections 4 and 5.4) derives general preimage recurrences for Rule 22 on finite spatial blocks and discusses the growth of maximal probabilities. That analysis gives essential context but does not state or prove the **unique all-zero modal output and exact maximum for all indexed finite periodic rings**. Gravner and Griffeath (first publicly online 10 December 2010) study Exactly 1 dynamics from finite seeds, replication, and periodicity, rather than this one-step finite-ring output-distribution extremum. Martínez and collaborators (2019) study Rule 22's de Bruijn graph, regular languages and dynamic patterns without giving this global modal-fiber theorem. The present proof exploits a new common componentwise envelope for arbitrary prescribed cyclic output patterns. These are implication comparisons, not an assertion of comprehensive priority certification.

## Limitations
The theorem is specific to a single synchronous Rule-22 update on indexed binary rings of length at least three. It does not classify runner-up outputs, determine the complete fiber distribution, extend to multiple iterations, or imply any corresponding result for other cellular automaton rules. The original literature contains general preimage machinery from which some related quantities could be derived; unindexed priority coverage remains possible.

## References
- E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf .
- J. Gravner and D. Griffeath, *The One-Dimensional Exactly 1 Cellular Automaton: Replication, Periodicity, and Chaos from Finite Seeds*, Journal of Statistical Physics **142** (2011), 168–200; published online 2010-12-10, https://doi.org/10.1007/s10955-010-0103-9 .
- G. J. Martínez et al., *On Patterns and Dynamics of Rule 22 Cellular Automaton*, Complex Systems **28** (2019), 125–174, https://doi.org/10.25088/ComplexSystems.28.2.125 .
