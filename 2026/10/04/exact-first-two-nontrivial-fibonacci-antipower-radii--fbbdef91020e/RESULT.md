# Exact first two nontrivial Fibonacci antipower radii
## Finding
Let \(\mathbf f=010010100100101\cdots\) be the Fibonacci word, the fixed point beginning in \(0\) of
\[
0\mapsto01,\qquad 1\mapsto0.
\]
For \(i\ge0\) and \(k\ge2\), let \(\gamma_i(k)\) be the least positive integer \(m\) for which
\[
\mathbf f[i\,..\,i+km)
\]
is a \(k\)-antipower when divided into \(k\) consecutive blocks of common length \(m\). Define
\[
R_{\mathbf f}(k)=\max_{i\ge0}\gamma_i(k).
\]
Then
\[
R_{\mathbf f}(3)=6,\qquad R_{\mathbf f}(4)=10.
\]

For \(k=3\), a sharp witness begins at zero-based index \(3\):
\[
010100100101001010.
\]
For block lengths \(1,2,3,4,5\), at least two of the three consecutive blocks coincide, while at block length \(6\) the blocks are
\[
010100,\qquad100101,\qquad001010,
\]
which are pairwise distinct.

For \(k=4\), the unique length-\(40\) factor whose minimum is \(10\) is
\[
0100101001001010010100100101001010010010,
\]
and it begins at zero-based index \(21\). At block length \(10\), its four blocks are
\[
0100101001,\qquad0010100101,\qquad0010010100,\qquad1010010010,
\]
which are pairwise distinct; no smaller positive block length gives four distinct blocks.

## Assumptions and scope
A \(k\)-antipower is a concatenation of \(k\) pairwise distinct words of equal length. The indexing convention is zero-based, matching Garg's convention for factors of the Fibonacci word.

The Fibonacci word is Sturmian. Therefore, for each positive integer \(N\), it has exactly \(N+1\) distinct factors of length \(N\). This standard Sturmian property is the finite-exhaustion bridge used below.

The claim concerns the exact uniform radii only for \(k=3\) and \(k=4\). It does not assert a formula for \(R_{\mathbf f}(k)\) at larger \(k\).

## Proof
For \(k=3\), it is enough to inspect length-\(18\) factors. Any starting index \(i\) determines one such factor, and whether \(\gamma_i(3)\le6\) depends only on these \(18\) symbols.

The bundled certificate contains \(19\) distinct length-\(18\) factors observed in the Fibonacci fixed point. Because \(\mathbf f\) is Sturmian, there are exactly
\[
18+1=19
\]
such factors in the entire infinite word. Hence the list is exhaustive. Direct comparison of the three consecutive blocks for each candidate block length \(m\in\{1,\ldots,6\}\) gives the distribution
\[
\#\{u:\gamma_u(3)=m\}=
\begin{cases}
8,&m=2,\\
4,&m=3,\\
1,&m=4,\\
2,&m=5,\\
4,&m=6.
\end{cases}
\]
Thus every index starts a \(3\)-antipower with block length at most \(6\), and some indices require \(6\). Therefore
\[
R_{\mathbf f}(3)=6.
\]

For \(k=4\), the same argument uses length-\(40\) factors. The certificate contains \(41\) distinct observed factors, and Sturmian complexity shows that these are all of them. Their exact minimum-block-length distribution is
\[
\#\{u:\gamma_u(4)=m\}=
\begin{cases}
4,&m=3,\\
2,&m=4,\\
4,&m=5,\\
27,&m=6,\\
2,&m=7,\\
1,&m=9,\\
1,&m=10.
\end{cases}
\]
Consequently every index starts a \(4\)-antipower with block length at most \(10\), and the displayed factor beginning at index \(21\) requires \(10\). Hence
\[
R_{\mathbf f}(4)=10.
\]

This is a finite proof once the standard Sturmian factor-complexity theorem is invoked: the certificate reaches the exact total \(N+1\) of possible length-\(N\) factors, so there is no unexamined infinite tail.

## Verification
Run `python3 verify.py` in the package directory. The checker regenerates the Fibonacci fixed point from the morphism, reconstructs every certified length-\(18\) and length-\(40\) factor, verifies that the lists contain respectively \(19\) and \(41\) distinct factors, recomputes every minimum block length, checks both histograms, and explicitly verifies the two sharp witnesses.

The checker relies on the proved Sturmian fact that the Fibonacci word has exactly \(N+1\) factors of length \(N\). Its finite enumeration is therefore exhaustive rather than a stabilization heuristic.

## Relationship to prior work
Garg proved that there is a constant \(c\le4\varphi/\sqrt5\approx2.89\) such that, for every \(k\) and every index of the Fibonacci word, a \(k\)-antipower begins there with block length at most \(ck\). He also introduced \(\gamma_i(k)\), the minimum block length at a fixed index, and derived asymptotic lower and upper bounds for \(\gamma_i(k)/k\). The same paper recalls that the Fibonacci word is Sturmian. It does not state exact values of the uniform maximum \(R_{\mathbf f}(k)\) for \(k=3\) or \(k=4\).

Berger and Defant formulated the linear-block-length conjecture for well-behaved morphic words and, in the published update, identify Garg's Fibonacci theorem as the first such result for a non-uniform morphic fixed point. Their paper does not give the two exact small-\(k\) radii.

Targeted searches for the exact phrases “Fibonacci word 3-antipower block length 6”, “Fibonacci word exact antipower constant \(k=3\)”, “Fibonacci word \(k\)-antipower optimal constant block length”, “antipowers Fibonacci word small \(k\) exact”, and “Fibonacci 4-antipower block length 10” did not locate a published result implying these two values.

## Limitations
The theorem gives only the first two nontrivial values of the uniform radius function \(R_{\mathbf f}(k)\). It does not improve Garg's asymptotic constant for arbitrary \(k\), nor does it address the prefix-only conjecture in the final section of that paper.

The originality search cannot exclude an unindexed computation, thesis, or note using equivalent terminology. The factor census itself is exact and independently reproducible from the bundled files.

## References
1. S. Garg, “Antipowers in Uniform Morphic Words and the Fibonacci Word,” arXiv:1907.10816, first public version 2019-07-25; Discrete Mathematics & Theoretical Computer Science 23:3 (2021), article 14, DOI 10.46298/dmtcs.7134.
2. A. Berger and C. Defant, “On anti-powers in aperiodic recurrent words,” Advances in Applied Mathematics 121 (2020), 102104, DOI 10.1016/j.aam.2020.102104.
