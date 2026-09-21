# Exact storage on the fifth-offset diagonal for retrieval requirement six

## Result

Let \(N(n,k,m)\) denote the minimum total storage of a \(t=1\) combinatorial batch code (CBC) with \(n\) items, retrieval requirement \(k\), and \(m\) servers. Then, for every integer \(m\ge 10\),

\[
\boxed{N(m+5,6,m)=m+18.}
\]

Thus the exact \(k=6\) storage function on the diagonal \(n=m+5\) is determined for all \(m\ge 10\).

## Background

In the dual set-system formulation, each item is represented by the set of servers on which it is stored. The CBC condition for \(t=1\) is the restricted Hall condition: the union of any \(r\le k\) item supports has size at least \(r\).

Jia, Zhang and Yuan proved
\[
N(m+3,6,m)=m+13\qquad(m\ge 8),
\]
and Shen, Jia and Zhang later proved
\[
N(m+4,6,m)=m+16\qquad(m\ge 8).
\]
The latter paper also records the two monotonicity facts used below: an optimal CBC with \(2\le k\le m<n\) has an item of degree at least two, and deleting an item of degree \(d\ge2\) gives
\[
N(n+1,k,m)\ge N(n,k,m)+d.
\]

## Proof

### Lower bound

Fix \(m\ge10\), and take an optimal \((m+5,N,6,m)\)-CBC. Since
\[
2\le 6\le m<m+5,
\]
the degree lemma gives an item of degree \(d\ge2\). Applying the deletion inequality and the known exact value on the preceding diagonal,
\[
N(m+5,6,m)
   \ge N(m+4,6,m)+d
   \ge (m+16)+2
   =m+18.
\]

### A base code at \(m=10\)

Use ten servers \(1,\dots,10\). In dual notation, let the fifteen item supports be
\[
\begin{aligned}
&\{3\},\{1,4\},\{2,4\},\{4,5\},\{5,6\},\{1,7\},\{2,7\},\{6,7\},\\
&\{1,8\},\{6,8\},\{9\},\{5,9\},\{2,10\},\{3,10\},\{8,10\}.
\end{aligned}
\]
Their total size is \(28\).

Equivalently, in the usual server-block notation the ten servers contain
\[
\begin{aligned}
B_1&=\{2,6,9\},&
B_2&=\{3,7,13\},&
B_3&=\{1,14\},&
B_4&=\{2,3,4\},&
B_5&=\{4,5,12\},\\
B_6&=\{5,8,10\},&
B_7&=\{6,7,8\},&
B_8&=\{9,10,15\},&
B_9&=\{11,12\},&
B_{10}&=\{13,14,15\}.
\end{aligned}
\]

The restricted Hall condition can be checked exactly on this finite system. For request sizes \(r=1,\dots,6\), the minimum cardinality of the union of any \(r\) item supports is respectively
\[
1,2,3,4,5,6.
\]
Hence this is a \((15,28,6,10)\)-CBC. The accompanying verification artifact checks all
\[
\sum_{r=1}^{6}\binom{15}{r}=9948
\]
request subsets.

### Extension to every \(m\ge10\)

Let \(p=m-10\). Add \(p\) new servers and \(p\) new items, placing each new item alone on its own new server. Repeated singleton extension preserves the retrieval requirement and increases both the number of items and total storage by one at each step. Starting from the base code therefore gives
\[
(15+p,\,28+p,\,6,\,10+p)
 =(m+5,\,m+18,\,6,\,m).
\]
Thus
\[
N(m+5,6,m)\le m+18.
\]
Together with the lower bound, this proves the theorem.

## Significance

The known exact \(k=6\) sequence \(n=m+3\) and \(n=m+4\) is extended by one further offset. The proof isolates the problem to a single small base construction: once the \((15,28,6,10)\)-CBC is available, published monotonicity supplies the matching lower bound and singleton extension propagates the construction to an infinite family.

## Limitations

- The theorem is asserted only for \(m\ge10\); it does not determine the boundary cases \(m=8,9\) on the \(n=m+5\) diagonal.
- Originality is to the best of our knowledge, based on searches for the exact formula, the base parameters \((15,28,6,10)\), synonymous CBC/Hall formulations, the 2016 and 2018 exact-diagonal papers, the 2019 \(k=5\) continuation, a 2023 CBC survey, and later generalized-CBC literature.
- The 2026 paper *On generalized combinatorial batch codes* was inspectable only through bibliographic metadata and its abstract. That abstract describes a broader failure/multiset model and special parameter regimes, and does not state the ordinary-CBC equality above; its uninspected full text remains a residual originality risk.

## References

1. M. B. Paterson, D. R. Stinson, R. Wei, *Combinatorial batch codes*, Advances in Mathematics of Communications 3 (2009), 13–27. https://doi.org/10.3934/amc.2009.3.13
2. C. Bujtás, Z. Tuza, *Optimal batch codes: Many items or low retrieval requirement*, Advances in Mathematics of Communications 5 (2011), 529–541. https://doi.org/10.3934/amc.2011.5.529
3. D. Jia, G. Zhang, L. Yuan, *A Class of Optimal Combinatorial Batch Code*, Acta Mathematica Sinica, Chinese Series 59 (2016), 267–278. https://doi.org/10.12386/A2016sxxb0024
4. Y. Shen, D. Jia, G. Zhang, *The results on optimal values of some combinatorial batch codes*, Advances in Mathematics of Communications 12 (2018), 681–690. https://doi.org/10.3934/amc.2018040
5. D. Jia, G. Zhang, *Some optimal combinatorial batch codes with k=5*, Discrete Applied Mathematics 262 (2019), 127–137. https://doi.org/10.1016/j.dam.2019.02.031
6. D. Jia, Y. Shen, G. Zhang, *A survey of the study of combinatorial batch code*, Frontiers of Mathematics in China 18 (2023), 301–312. https://doi.org/10.3868/s140-DDD-023-0024-x
7. Z. Guo, G. Zhang, *On generalized combinatorial batch codes*, Discrete Applied Mathematics 391 (2026), 57–67. https://doi.org/10.1016/j.dam.2026.04.038
