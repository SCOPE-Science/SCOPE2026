# Exact ternary length-five single-deletion code size

## Finding
Let \(B_3=\{0,1,2\}\), and for a word \(x\in B_3^5\) let \(D_1(x)\subseteq B_3^4\) be the set of distinct words obtained by deleting one coordinate of \(x\). A code \(C\subseteq B_3^5\) corrects one deletion when the sets \(D_1(x)\), for \(x\in C\), are pairwise disjoint. If \(N(5,3,1)\) denotes the maximum possible size of such a code, then
\[
N(5,3,1)=24.
\]
An extremal code is

```text
00000 00011 00022 00120 01110 01212 02021 02100 02220 10102 10211 11000 11111 11122 11201 12020 12221 20101 21022 21210 22000 22012 22111 22222
```

## Assumptions and scope
The channel is the standard ordered-word single-deletion channel: exactly one coordinate may be deleted, and the receiver observes the remaining four symbols in their original order. Repeated deletions that produce the same length-four word count only once in \(D_1(x)\). No linearity, cyclicity, or algebraic structure is assumed for the code.

## Proof
The displayed 24 words give the lower bound. The standalone verifier forms every distinct deletion shadow and checks that the 24 shadows are pairwise disjoint.

For the upper bound, assign each length-four ternary word \(z\) a nonnegative rational weight \(y_z\). The exact certificate embedded in `verify.py` writes \(y_z=c_z/14\), where each \(c_z\) is a positive integer. It verifies, for every one of the \(3^5=243\) possible length-five ternary words \(x\), that
\[
\sum_{z\in D_1(x)}c_z\ge14.
\]
It also verifies
\[
\sum_{z\in B_3^4}c_z=348.
\]
If \(C\) is any one-deletion-correcting code, its deletion shadows are disjoint, so summing the first inequality over \(x\in C\) cannot use any output weight more than once. Hence
\[
14|C|\le348,
\]
and therefore
\[
|C|\le\left\lfloor\frac{348}{14}\right\rfloor=24.
\]
Together with the displayed code, this proves the equality.

The same certificate is a feasible dual solution for the standard fractional set-packing relaxation, with objective \(348/14=174/7\). Its value is strictly below \(25\), which is enough to force the integral optimum to be at most \(24\).

## Verification
Running `python3 verify.py` uses only the Python standard library. It reconstructs all \(81\) possible length-four deletion outputs and all \(243\) length-five input words, checks the 24-word code directly, checks every one of the 243 dual-cover inequalities, and checks the exact integer numerator sum \(348\). The expected final line is

```text
VERIFY_OK N(5,3,1)=24 dual=174/7 min_scaled_shadow_weight=14
```

The generated `certificate.json` records the checked counts and the exact dual objective. No floating-point optimization or solver output is needed to replay the proof.

## Relationship to prior work
Kulkarni and Kiyavash formulate deletion codes as hypergraph matchings and give a numerical fractional-matching table. For the exact row \(q=3\), \(n=5\), their Table I reports the integer-rounded fractional upper bound \(24\), while the largest Tenengolts-family code known to them has size \(17\). Thus that source supplies a strong upper-bound benchmark but not an exact value or a size-24 construction. The rational certificate here independently verifies the upper bound without relying on their numerical computation, and the displayed 24-word code closes the recorded gap.

A later exact computation for the different parameter \(q=5\), \(n=4\) obtains \(N(4,5,1)=42\); it does not imply the ternary length-five value. Searches under single-deletion, insertion-deletion, hypergraph matching, Tenengolts, and exact-parameter terminology did not identify an indexed source stating \(N(5,3,1)=24\).

## Limitations
This is an exact finite-parameter result. It does not classify all optimal 24-word codes, give a general formula in \(q\) or \(n\), or improve the asymptotic theory of deletion codes. Bibliographic residual risk remains because a 2012 conference paper by Li and Houghten reports computational experiments on nonbinary Tenengolts codes, but its full text was not available in the material inspected here.

## References
1. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128, first posted 2012-11-13; later *IEEE Transactions on Information Theory* 59(8) (2013), 5115–5130, DOI 10.1109/TIT.2013.2257917.
2. Z. Li and S. K. Houghten, “Searching for Optimal Deletion Correcting Codes: New Properties and Extensions of Tenengolts Codes,” CIT 2012, 647–654, DOI 10.1109/CIT.2012.137.
3. “Exact quinary length-four single-deletion code size,” published record `2026/9/21/SCOPE-exact-quinary-length-four-single-deletion-code--77daafd66a03`.
