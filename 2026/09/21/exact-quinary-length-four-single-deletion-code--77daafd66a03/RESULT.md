# Exact quinary length-four single-deletion code size

## Result

Let \(B_q=\{0,1,\ldots,q-1\}\), and for a word \(x\in B_q^4\) let
\(D_1(x)\subseteq B_q^3\) be the set of distinct words obtained by deleting one coordinate of \(x\). A code \(C\subseteq B_q^4\) corrects one deletion exactly when the sets \(D_1(x)\), \(x\in C\), are pairwise disjoint. In the notation

\[
N(4,q,1)=\max\{|C|:C\subseteq B_q^4\text{ corrects one deletion}\},
\]

the quinary value is

\[
\boxed{N(4,5,1)=42.}
\]

The classical length-four bound gives \(N(4,5,1)\le45\). Thus the exact value improves that upper bound by three codewords.

## Lower bound

The following 42 words form a one-deletion-correcting code over \(B_5\):

```text
0000 0011 0022 0033 0044 0120 0213 0340 1043 1100 1111 1122 1133 1144
1231 1302 1401 2014 2032 2200 2211 2222 2233 2244 2412 2430 3041 3124
3300 3311 3322 3333 3344 3423 4024 4134 4321 4400 4411 4422 4433 4444
```

Direct enumeration of the distinct one-deletion shadows verifies that no two listed words share a length-three deletion output. Hence

\[
N(4,5,1)\ge42.
\]

## Exact upper bound

The upper bound has a finite set-packing formulation. Introduce one binary variable \(x_w\) for every \(w\in B_5^4\). For every \(y\in B_5^3\), impose

\[
\sum_{w:\,y\in D_1(w)}x_w\le1.
\]

There are \(5^4=625\) binary variables and \(5^3=125\) capacity constraints. The objective is

\[
\max\sum_{w\in B_5^4}x_w.
\]

This integer program is exactly equivalent to the coding problem: a feasible 0-1 solution selects words whose deletion shadows are pairwise disjoint, and every one-deletion-correcting code gives such a feasible solution.

The standalone verification artifact solves this finite integer program to a zero mixed-integer gap and obtains matching primal and dual bounds 42. It also verifies the displayed 42-word witness independently. Consequently

\[
N(4,5,1)\le42,
\]

which proves the stated equality.

As a model sanity check, the same formulation returns \(N(4,4,1)=24\), agreeing with the published even-alphabet formula.

## Literature context

Kim, Lee, and Oh proved the sharp length-four formula for every even alphabet size. Their Theorem 2.2 reduces to the earlier Levenshtein bound for odd \(q\), and their Remark 1 explicitly states that this odd-alphabet bound is not sharp and that obtaining a sharp bound for odd \(q\) appears difficult. For \(q=5\), that bound is

\[
\left\lfloor\frac{5^3+2\cdot5^2+5}{4}\right\rfloor=45.
\]

Wang and Ji proved existence of perfect \(T^*(3,4,v)\) deletion codes for odd \(v\), but perfect deletion codes can have different cardinalities because deletion shadows have nonuniform sizes; existence of a perfect code therefore does not determine the maximum cardinality considered here.

Kulkarni and Kiyavash later formulated optimal deletion codes as hypergraph matchings and integer programs and derived general nonasymptotic upper bounds, but their general bound does not determine this small parameter exactly.

To the best of our knowledge, the exact value \(N(4,5,1)=42\) has not previously been stated. Searches under the equivalent terminology of quinary single-deletion codes, length-four deletion/insertion metric codes, and hypergraph set-packing formulations did not identify a published exact value for this parameter.

A specific residual originality uncertainty is Li and Houghten, *Searching for Optimal Deletion Correcting Codes: New Properties and Extensions of Tenengolts Codes* (CIT 2012, DOI 10.1109/CIT.2012.137). Its bibliographic record and abstract were inspected; the full paper was not inspected. Because it reports computational experiments and extensions of nonbinary Tenengolts codes, it could in principle contain an unindexed small-parameter observation relevant to \(q=5,n=4\). The originality claim is therefore only to the best of our knowledge.

## Reproducibility

`artifacts/verify_q5.py` constructs the exact set-packing integer program, verifies the displayed 42-word code, checks the known \(q=4\) value as a sanity test, and solves the \(q=5\) instance. `artifacts/verification_output.txt` records the verified output. The computation uses SciPy 1.17.0's mixed-integer optimization interface to HiGHS with binary integrality constraints and zero requested relative MIP gap.

## Limitations

The matching upper bound is computer-assisted rather than a short symbolic classification of odd-alphabet length-four codes. It determines the first concrete quinary instance \(q=5\) but does not give a general sharp formula for all odd \(q\). The result concerns the standard ordered-word deletion channel; it does not apply to multiset deletion models or constrained synchronization channels.

**Same-model review: passed. Independent audit: not yet performed.**

## References

1. H. K. Kim, J. Y. Lee, and D. Y. Oh, “Optimal single deletion correcting code of length four over an alphabet of even size,” *IEEE Transactions on Information Theory* 56(7) (2010), 3217–3220. https://doi.org/10.1109/TIT.2010.2048492 ; preprint: https://arxiv.org/abs/1003.4057
2. J. Wang and L. Ji, “Existence of T*(3,4,v)-codes,” *Journal of Combinatorial Designs* 13(1) (2005), 42–53. https://doi.org/10.1002/jcd.20031
3. A. A. Kulkarni and N. Kiyavash, “Nonasymptotic upper bounds for deletion correcting codes,” *IEEE Transactions on Information Theory* 59(8) (2013), 5115–5130. https://doi.org/10.1109/TIT.2013.2257917 ; preprint: https://arxiv.org/abs/1211.3128
4. Z. Li and S. K. Houghten, “Searching for Optimal Deletion Correcting Codes: New Properties and Extensions of Tenengolts Codes,” *CIT 2012*, 647–654. https://doi.org/10.1109/CIT.2012.137
