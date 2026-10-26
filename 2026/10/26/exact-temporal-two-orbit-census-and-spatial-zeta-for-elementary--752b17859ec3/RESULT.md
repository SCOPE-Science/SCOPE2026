# Exact temporal-two orbit census and spatial zeta for elementary cellular automaton 18

## Finding

Let \(F\) be elementary cellular automaton 18, and let \(F_n\) act on the binary cyclic ring \(\mathbb Z/n\mathbb Z\), for each integer \(n\geq1\). Define \(a_n=\#\{x:F_n^2x=x\}\), and let \(c_n\) count distinct exact temporal two-cycles (unordered pairs of configurations). Then

\[
\boxed{\exp\bigl(\sum_{n\ge1}a_nz^n/n\bigr)=\frac{1}{(1-z)(1-z^4-2z^5-z^6)}.}
\]

More explicitly, \(a_n=1+b_n\), with \(b_1=b_2=b_3=b_7=0\), \(b_4=4\), \(b_5=10\), \(b_6=6\), and

\[
b_n=b_{n-4}+2b_{n-5}+b_{n-6}\qquad(n\ge7).
\]

The only fixed configuration of \(F_n\) is all-zero, so \(c_n=b_n/2\). Thus a nontrivial temporal two-cycle exists **if and only if**

\[
n\in\{4,5,6\}\cup\{8,9,10,\ldots\}=\langle4,5,6\rangle.
\]

In particular, spatial length seven is the last exceptional length. The shift of the full bi-infinite temporal-two subshift \(Y=\{x:F^2x=x\}\) has topological entropy \(\log\rho\), where \(\rho>1\) is the real root of \(\rho^3-\rho-1=0\). In particular \(b_n=\rho^n+O(1.30^n)\).

## Assumptions and scope

The binary local rule is \(f(u,v,w)=1\) precisely for triples \(001\) or \(100\), and is zero for the other six triples. All spatial indices are cyclic on \(\mathbb Z/n\mathbb Z\); for \(n=1,2\), repeated neighbor positions use the same cyclic convention. Temporal period means iteration of \(F_n\), not spatial shift. The formal power series identity is around \(z=0\). The set \(Y\) is a closed shift-invariant subshift of the full binary shift.

## Proof

**1. Local finite-type constraint.** For a five-bit word \(w=w_0w_1w_2w_3w_4\), compute

\[
g(w)=f\bigl(f(w_0,w_1,w_2),f(w_1,w_2,w_3),f(w_2,w_3,w_4)\bigr).
\]

The condition \(F^2x=x\) is equivalent to \(g(x_{i-2}\ldots x_{i+2})=x_i\) for every \(i\). Exhausting the 32 words gives exactly 20 admissible words. These are

`00000 00010 00011 00101 00110 00111 01000 01001 01010 01011 01100 10001 10010 10011 10100 11000 11001 11010 11011 11100`.

Build the directed de Bruijn graph with all 16 four-bit vertices and an edge from \(w_0w_1w_2w_3\) to \(w_1w_2w_3w_4\) for each admissible five-bit word. Write \(M\) for the 16-by-16 adjacency matrix. A cyclic walk of length \(n\) is exactly a labelled spatially \(n\)-periodic element of \(Y\), even for \(n<5\), because the cyclic overlaps enforce the same repeated coordinates. Therefore \(a_n=\operatorname{tr}(M^n)\) for every \(n\ge1\).

**2. Exact finite graph calculation.** Besides the singleton loop at `0000`, the only directed cycles are contained in the ten-vertex set

`0001 0010 0011 0100 0101 0110 1000 1001 1010 1100`.

Its directed edges (from, to) are

`0001:0010,0011; 0010:0101; 0011:0110; 0100:1000,1001; 0101:1010; 0110:1100; 1000:0001; 1001:0010,0011; 1010:0100; 1100:1000,1001`.

Enumerating elementary directed cycles in this ten-vertex graph gives one cycle of length four, two of length five, one of length six, and two of length ten. The only pairs of vertex-disjoint elementary cycles are the four- plus six-cycle and the pair of five-cycles. Both have combined length ten. By the elementary-cycle expansion of the determinant, the contributions of the two length-ten cycles cancel these two disjoint pairs. Thus the determinant for the ten-vertex component is exactly \(1-z^4-2z^5-z^6\); vertices on no directed cycle contribute a factor one. The isolated all-zero loop contributes \(1-z\). Consequently,

\[
\det(I-zM)=(1-z)(1-z^4-2z^5-z^6).
\]

The explicit graph is reproduced by the standalone standard-library verifier, which independently enumerates all directed elementary cycles and all vertex-disjoint selections; the determinant identity is an exact finite calculation, not an asymptotic inference.

**3. Zeta, recurrence and existence.** The formal determinant identity

\[
-\log\det(I-zM)=\sum_{n\ge1}\operatorname{tr}(M^n)z^n/n
\]

proves the displayed zeta formula. Let \(b_n=a_n-1\). The six nonzero characteristic roots other than the all-zero fixed-loop eigenvalue obey \(\lambda^6-\lambda^2-2\lambda-1=0\). Their power sums give the stated initial conditions and length-six recurrence with lags four, five and six. Directly, \(b_4=4\), \(b_5=10\), \(b_6=6\); then \(b_7=0\), while \(b_8=4\), \(b_9=18\), \(b_{10}=30\), \(b_{11}=22\). Thereafter, \(b_n\ge b_{n-4}>0\) for all \(n\ge12\), by induction. This proves the precise missing-length classification.

Every output `1` of \(f\) comes from an input triple with central symbol `0`. Thus \(F_nx=x\) forces \(x\) to have no `1`, proving that the all-zero configuration is the sole temporal fixed point. All \(b_n\) other members of \(\operatorname{Fix}(F_n^2)\) occur in exact two-cycles, hence \(c_n=b_n/2\).

Finally the sextic factors as \((\lambda^3-\lambda-1)(\lambda^3+\lambda+1)\). The first factor has a unique positive real root \(\rho\approx1.324718\), which exceeds in modulus its complex pair. The second has a negative real root \(-t\) with \(0.6<t<1\), and its complex pair has modulus \(t^{-1/2}<1.30\); also \(\rho>1.30\). Hence \(\rho\) is the unique maximal-modulus eigenvalue of \(M\), and standard finite-state symbolic-dynamics entropy gives \(h_{\mathrm{top}}(\sigma|_Y)=\log\rho\). The same root comparison gives the stated error term.

## Verification

Run `python3 verify.py` using Python 3 standard library. Its assertions derive all 20 allowed local words directly from the eight-case rule, enumerate the de Bruijn graph's elementary cycles and vertex-disjoint collections, and compute the determinant polynomial by exact signed integer arithmetic. It verifies the recurrence and tests all configurations directly on every ring \(1\le n\le15\), reporting `VERIFY_OK`. This finite replay checks the critical graph certificate independently of the written list; universality for all ring lengths follows from the exact transfer-graph and determinant proof, not from bounded enumeration.

## Relationship to prior work

Zhu and Richard (arXiv:2610.10967v1; posted 2026-10-07) classify finite-ring Koopman spectra and specifically place rule 18 in a four-rule spectral family on sizes 13 through 27; their classification does not imply an all-length exact enumeration of temporal-two points, an exact spatial zeta function, or the excluded-length set. Stricker (2023) classified elementary automata by their *longest* cycle lengths, with numerical finite-ring data for rule 18; that quantity does not determine the multiplicities of length-two orbits or their spatial generating function. Sabrié and Törmä (arXiv:2308.12744, posted 2023-08-24) analyze limit sets and kink dynamics of rule 18 and exhibit an example of an exact temporal two-cycle on a four-periodic configuration; this demonstrates one instance but does not imply the complete all-ring census. The present result computes a different dynamical invariant, with exact counts at every ring length.

## Limitations

This theorem concerns only exact temporal periods one and two for rule 18, not its higher temporal periods or complete long-term finite-ring behavior. The spatial zeta pertains to the *restriction* \(Y=\operatorname{Fix}(F^2)\), not the zeta of all temporally recurrent points or the full cellular automaton. Historical priority under alternative automata terminology remains a risk; no independent scientific audit has occurred.

## References

1. Q. Zhu and S. Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations*, arXiv:2610.10967v1 (first public 2026-10-07), https://arxiv.org/abs/2610.10967 .
2. H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, Complex Systems 32 (2023), 229–251, https://doi.org/10.25088/ComplexSystems.32.3.229 .
3. H. Sabrié and I. Törmä, *Limit dynamics of elementary cellular automaton 18*, arXiv:2308.12744 (first public 2023-08-24), https://arxiv.org/abs/2308.12744 .
