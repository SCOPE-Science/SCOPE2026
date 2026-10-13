# Exact optimum for five-cell ternary single downward limited-magnitude codes

## Finding
Let \(\mathcal X=\{0,1,2\}^{5}\), and let a transmission either be received without error or undergo a decrease of exactly one level in **one** coordinate. The maximum cardinality of any zero-error correcting code is
\[
\max\{|C|:C\subseteq\mathcal X,\ B(x)\cap B(z)=\varnothing\ (x\ne z\in C)\}=45.
\]
This sharpens the previously published fractional-packing upper bound of \(55\) for the same channel and parameters. The optimum is attained by the explicitly listed code in `data/codewords.txt`.

## Assumptions and scope
All five positions are labeled. Levels are the integers \(0,1,2\) without cyclic wraparound. The error budget is **at most one** downward step of magnitude exactly one; the no-error outcome is included. For \(x=(x_1,\ldots,x_5)\), define
\[
B(x)=\{x\}\cup\{x-e_i:1\le i\le5,\ x_i>0\}.
\]
No linearity, cyclicity, systematic encoding, or prescribed decoding architecture is assumed. Coordinate reflection \(x_i\mapsto2-x_i\) gives an equivalent upward-error problem.

## Proof
Disjointness of all received sets \(B(x)\) is necessary and sufficient for zero-error correction, because two messages sharing a possible received word could not always be distinguished. There are \(3^5=243\) input words and 243 possible received words.

For every received word \(y\), define its set of possible senders \(R(y)=\{x\in\mathcal X:y\in B(x)\}\). Introduce one Boolean variable \(z_x\) per input word. The maximum code size is **exactly** the optimal integer-program objective
\[
\max\sum_{x\in\mathcal X}z_x\quad\text{subject to}\quad \sum_{x\in R(y)}z_x\le1\ (y\in\mathcal X),\quad z_x\in\{0,1\}.
\]
The equivalence holds both ways: any code is a feasible selection, and any feasible selection has disjoint error balls.

The standalone integer optimization in `tools/solve_packing.py` constructs the entire 243-by-243 receiver-incidence matrix directly from this definition. Running HiGHS through SciPy returns **optimal** status, feasible objective \(45\), dual upper bound \(45\), and zero relative mixed-integer gap. Independently, `tools/solve_pairs.py` constructs the confusability graph by joining two distinct senders precisely when their received balls intersect; there are 243 vertices and 1890 edges. Its independent-set integer program also returns global optimum \(45\) with coincident primal and dual bounds. These are two equivalent integer formulations built separately, not a symbolic closed-form inequality certificate.

Finally, `data/codewords.txt` supplies 45 distinct codewords. The standard-library checker `tools/verify_code.py` enumerates every possible received word of each listed codeword, verifies pairwise disjointness, and finds 185 distinct possible outputs. Thus the lower bound is checked independently of integer optimization. The equality \(45\) follows from that construction and the globally optimal upper computations, conditional on the mathematical and computational correctness of the mixed-integer solver.

## Verification
From the directory containing this document, run:

```
python tools/verify_code.py
python tools/solve_packing.py
python tools/solve_pairs.py
```

The first script requires only Python's standard library. The remaining scripts require `numpy` and `scipy` with HiGHS mixed-integer optimization enabled. Both require solver status `optimal`, a matching primal objective and dual bound of \(45\), and negligible numerical reported gap. A mere solver timeout or a feasible solution does not establish optimality. All three scripts were executed and returned the expected results.

## Relationship to prior work
Fazeli, Vardy and Yaakobi, *Generalized Sphere Packing Bound* (2014), Section V.A, define the same single asymmetric limited-magnitude channel and derive fractional packing bounds. Their Table V, row \(q=3,n=5\), lists a generalized sphere-packing upper bound of \(55\); no exact integer optimum of \(45\) appears there. Buzaglo and Etzion (2011) investigate lattice/perfect-code existence for asymmetric limited-magnitude errors rather than an unrestricted optimal cardinality for this finite box. Cassuto, Schwartz, Bohossian and Bruck (2010) construct such codes and study bounds and asymptotics; an available abstract did not establish the requested exact value. The result concerns unrestricted finite non-linear packing, rather than the performance of a particular systematic construction.

## Limitations
The theorem is confined to three levels, five cells, and at most one one-step error. It does not classify all maximum codes, nor extend to higher block lengths. The integer upper bound depends on the correctness of the external branch-and-bound implementation; an independently checkable formal integer infeasibility certificate was not generated. A relevant full 2011 paper on systematic limited-magnitude coding and other historical publications were not completely inspected. Consequently an undiscovered prior exact enumeration remains possible; absence of an accessible match is not a proof of priority.

## References
1. A. Fazeli, A. Vardy, E. Yaakobi, *Generalized Sphere Packing Bound*, arXiv:1401.6496v1 (2014), Section V.A and Table V. https://arxiv.org/pdf/1401.6496
2. S. Buzaglo, T. Etzion, *On the Existence of Perfect Codes for Asymmetric Limited-Magnitude Errors*, arXiv:1112.0896v2 (2011). https://arxiv.org/pdf/1112.0896
3. Y. Cassuto, M. Schwartz, V. Bohossian, J. Bruck, *Codes for Asymmetric Limited-Magnitude Errors with Application to Multilevel Flash Memories*, IEEE Transactions on Information Theory **56** (2010), 1582–1595, doi:10.1109/TIT.2010.2040971.
4. T. Kløve, B. Bose, N. Elarief, *Systematic, Single Limited Magnitude Error Correcting Codes for Flash Memories*, IEEE Transactions on Information Theory (2011), doi:10.1109/TIT.2011.2146330 (full text not inspected).
