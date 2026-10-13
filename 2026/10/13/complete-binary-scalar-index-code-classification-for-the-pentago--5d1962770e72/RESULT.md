# Complete binary scalar index-code classification for the pentagon

## Finding
For the five-receiver binary scalar unicast index-coding problem whose side-information graph is the cycle \(C_5\), with receiver \(i\) knowing \(x_{i-1}\) and \(x_{i+1}\) modulo \(5\), the minimum scalar linear codelength is \(3\). Up to invertible changes of the three transmitted coordinates, there are exactly \(20\) optimal binary linear codes. Under the natural dihedral automorphism group \(D_{10}\) of the side-information cycle, these \(20\) row spaces form exactly four orbits, each of size \(5\) and stabilizer order \(2\). Their four distinct Hamming weight enumerators are \(1+2z^2+4z^3+z^4\), \(1+3z^2+3z^3+z^5\), \(1+4z^2+3z^4\), and \(1+z+2z^2+2z^3+z^4+z^5\). Consequently there are exactly \(3360\) full-rank binary \(3\times5\) encoding matrices realizing optimal scalar linear codes.

A representative basis for each of the four dihedral orbits, with columns ordered \(0,1,2,3,4\), is
\[
\begin{aligned}
B_1&=\begin{pmatrix}1&1&0&0&0\\0&0&1&1&0\\1&0&1&0&1\end{pmatrix},\\
B_2&=\begin{pmatrix}1&1&0&0&0\\1&0&1&0&0\\1&0&0&1&1\end{pmatrix},\\
B_3&=\begin{pmatrix}1&1&0&0&0\\1&0&1&0&0\\0&0&0&1&1\end{pmatrix},\\
B_4&=\begin{pmatrix}1&0&0&0&0\\0&1&1&0&0\\0&0&0&1&1\end{pmatrix}.
\end{aligned}
\]
The corresponding weight enumerators, in the same order after sorting by enumerator, are \(1+2z^2+4z^3+z^4\), \(1+3z^2+3z^3+z^5\), \(1+4z^2+3z^4\), and \(1+z+2z^2+2z^3+z^4+z^5\).

## Assumptions and scope
There are five independent binary messages \(x_0,\ldots,x_4\). Receiver \(i\) requests \(x_i\) and knows exactly the two neighboring messages \(x_{i-1}\) and \(x_{i+1}\), with indices modulo \(5\). A scalar linear encoder is a binary matrix \(L\) whose transmitted word is \(Lx\). Two full-rank \(3\times5\) encoders are regarded as output-basis equivalent when their row spaces agree, equivalently when one is obtained from the other by left multiplication by an element of \(\operatorname{GL}(3,2)\). Natural instance symmetries are the rotations and reflections of \(C_5\), namely \(D_{10}\).

The finding concerns scalar binary linear coding only. It does not classify nonlinear encoders, vector linear encoders, or asymptotic broadcast-rate constructions.

## Proof
Let \(R\) be the row space of a binary encoder \(L\). Receiver \(i\) can recover \(x_i\) from \(Lx\) and its two side-information bits if and only if \(R\) contains a vector \(r_i\) with \(r_{i}=1\) and
\[
\operatorname{supp}(r_i)\subseteq\{i-1,i,i+1\}.
\]
Sufficiency is immediate: the receiver forms the corresponding linear combination of the transmitted coordinates and subtracts its known neighboring terms. For necessity, if \(x_i\) is determined by the linear observation \(Lx\) together with \(x_{i-1}\) and \(x_{i+1}\), then every vector in the common kernel of those observations has zero \(i\)-th coordinate. By finite-dimensional linear duality, \(e_i\) belongs to the row span of \(L\), \(e_{i-1}\), and \(e_{i+1}\), which rearranges to the stated witness \(r_i\).

Thus the problem is an exact finite classification of subspaces of \(\mathbb F_2^5\). The verifier enumerates every subspace in dimensions \(0\) through \(5\); the counts are \(1,31,155,155,31,1\). Applying the decoding criterion gives valid-subspace counts \(0,0,0,20,16,1\). Hence no scalar linear code of length below \(3\) exists, and exactly \(20\) three-dimensional row spaces are optimal.

As an independent formulation, choose for each receiver one fitting row of the form
\[
e_i+a_i e_{i-1}+b_i e_{i+1},\qquad a_i,b_i\in\mathbb F_2.
\]
There are exactly \(4^5=1024\) such fitting matrices. A separately implemented rank computation gives rank distribution \(45\) of rank \(3\), \(537\) of rank \(4\), and \(442\) of rank \(5\). The rank-\(3\) fitting matrices yield exactly the same \(20\) row spaces as the direct subspace census. Their multiplicities over those row spaces are \(1\) for five spaces, \(2\) for ten spaces, and \(4\) for five spaces.

Finally, applying all ten coordinate permutations in \(D_{10}\) to the \(20\) optimal row spaces produces four orbits of size \(5\). Orbit-stabilizer therefore gives stabilizer order \(2\) for every orbit. The four displayed Hamming weight enumerators are distinct, so the four orbit classes are pairwise inequivalent. Since \(\lvert\operatorname{GL}(3,2)\rvert=(8-1)(8-2)(8-4)=168\), each three-dimensional row space has \(168\) ordered bases, giving \(20\cdot168=3360\) full-rank encoding matrices.

## Verification
Run `python3 artifacts/verify.py`. The script uses two finite enumerations: direct subspace enumeration for the receiver-decoding criterion, and independent highest-pivot rank plus subset-XOR span routines for all fitting matrices. It then checks the full dihedral action, orbit sizes, stabilizers, representative bases, weight enumerators, and the \(\operatorname{GL}(3,2)\) matrix count.

The recorded terminal output ends with:

`VERIFY_OK min_linear_length=3 optimal_rowspaces=20 full_rank_3x5_encoders=3360 fitting_rank3=45 dihedral_orbits=4 orbit_sizes=5,5,5,5 stabilizer=2`

## Relationship to prior work
Bar-Yossef, Birk, Jayram, and Kol introduced minrank for index coding and proved that odd holes have optimal scalar linear codelength given by minrank; their odd-hole theorem specializes to codelength \(3\) for \(C_5\). Their pentagon discussion establishes optimal length but does not enumerate the minimizing binary row spaces or their symmetry classes. Ong later proved linear optimality for every zero-error unicast instance with at most five receivers; that theorem settles optimal codelengths across instances, not the equality classification of all binary scalar linear encoders for this fixed instance. Chlamtáč and Haviv study minrank algorithmically, while Esfahanizadeh, Lahouti, and Hassibi give a finite-field matrix-completion method; neither inspected source states the \(20\)-row-space census or four-orbit decomposition.

The present result is therefore an equality-layer refinement of the classical pentagon example: the optimum value itself is known, while the complete binary scalar linear optimizer set is classified here.

## Limitations
The finite verification proves only the stated five-message, one-bit, binary scalar linear classification. It does not imply that \(3\) is the asymptotic broadcast rate; vector and asymptotic formulations have different behavior. The originality comparison covers the inspected primary sources and targeted bibliographic searches, but an obscure unpublished or poorly indexed finite enumeration could still exist.

## References
1. Z. Bar-Yossef, Y. Birk, T. S. Jayram, and T. Kol, “Index Coding with Side Information,” FOCS 2006, pp. 197–206, DOI 10.1109/FOCS.2006.42.
2. E. Chlamtáč and I. Haviv, “Linear Index Coding via Semidefinite Programming,” arXiv:1107.1958v1; Combinatorics, Probability and Computing 23 (2014), DOI 10.1017/S0963548313000564.
3. L. Ong, “Linear Codes are Optimal for Index-Coding Instances with Five or Fewer Receivers,” arXiv:1401.7369v1; ISIT 2014, DOI 10.1109/ISIT.2014.6874881.
4. H. Esfahanizadeh, F. Lahouti, and B. Hassibi, “A Matrix Completion Approach to Linear Index Coding Problem,” arXiv:1408.3046v1; ITW 2014, DOI 10.1109/ITW.2014.6970888.
