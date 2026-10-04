# Exact length-three single-deletion covering number for odd alphabets
## Finding
For every odd integer \(q\ge 3\), the minimum size \(D(q,3,1)\) of a \(q\)-ary length-three single-deletion covering code is exactly
\[
D(q,3,1)=\left\lceil \frac{q^2}{3}\right\rceil.
\]
Here a codeword \((a,b,c)\) covers the length-two words \((a,b)\), \((a,c)\), and \((b,c)\), with repetitions identified.

## Assumptions and scope
The alphabet is any set \(\Sigma\) with odd cardinality \(q\ge 3\). A one-deletion covering code is a subset \(C\subseteq \Sigma^3\) whose deletion balls cover all of \(\Sigma^2\). The proof uses the published existence theorem of Colbourn and Rosa for quadratic leaves of partial triple systems. Their theorem supplies the needed triangle decomposition of a nearly complete graph; the translation of that decomposition into deletion-covering codewords is given explicitly below.

## Proof
Every length-three word has at most three distinct one-deletion descendants. Since \(|\Sigma^2|=q^2\), the elementary counting bound gives
\[
|C|\ge \left\lceil \frac{q^2}{3}\right\rceil.
\]
It remains to meet this bound for every odd \(q\).

For a partial triple system on \(q\) points, its leave is the graph formed by the unordered pairs not contained in any triple. Colbourn and Rosa proved that, apart from one irrelevant exception, every graph whose vertex degrees are zero or two and which satisfies the standard parity and divisibility conditions is the leave of a maximal partial triple system. Equivalently for the leaves used here, the complement of the leave decomposes into edge-disjoint triangles.

First suppose \(q\equiv 3\pmod 6\) and \(q\ge 9\). Take the desired leave to be a cycle \(L=C_q\). Its vertices all have degree two, and
\[
\binom q2-|E(L)|=\frac{q(q-3)}2
\]
is divisible by three. Thus \(K_q-L\) has a triangle decomposition \(\mathcal B\). For every block \(\{x,y,z\}\in\mathcal B\), choose an ordering \((x,y,z)\) and put both \((x,y,z)\) and \((z,y,x)\) into the code. Their deletion descendants are exactly the six directed versions of the three edges of that block. Orient the cycle cyclically as \(v_0,v_1,\ldots,v_{q-1},v_0\), and for each \(i\) add
\[
(v_i,v_{i+1},v_i).
\]
This word covers the loop \((v_i,v_i)\) and both directed versions of the cycle edge \(\{v_i,v_{i+1}\}\). Hence every ordered pair is covered. Since \(|\mathcal B|=q(q-3)/6\), the code has
\[
2|\mathcal B|+q=\frac{q^2}{3}
\]
words. The case \(q=3\) is direct: on symbols \(0,1,2\), the three words \((0,1,0)\), \((1,2,1)\), and \((2,0,2)\) cover all nine ordered pairs.

Now suppose \(q\equiv 1\) or \(5\pmod 6\). Let the leave be \(L=C_{q-1}\cup K_1\): a cycle on \(q-1\) points and one isolated point \(z\). Again every leave degree is zero or two, and
\[
\binom q2-|E(L)|=\frac{(q-1)(q-2)}2
\]
is divisible by three. The quadratic-leave theorem gives a triangle decomposition \(\mathcal B\) of \(K_q-L\). For each block add the same two opposite orderings as above. For each cycle vertex \(v_i\), add \((v_i,v_{i+1},v_i)\), and also add \((z,z,z)\). These codewords cover every directed leave edge and every loop. Therefore all of \(\Sigma^2\) is covered. Here \(|\mathcal B|=(q-1)(q-2)/6\), so the total number of codewords is
\[
2|\mathcal B|+q=\frac{q^2+2}{3}=\left\lceil\frac{q^2}{3}\right\rceil.
\]
The lower and upper bounds agree in every odd case.

## Verification
The included `verify_odd_q.py` checks the deletion-ball translation, the residue-class counts, and explicit triangle-decomposition witnesses for \(q\in\{3,5,7,9,11,13\}\). These computations are finite sanity checks; the all-odd existence step is supplied by the cited quadratic-leave theorem rather than by finite enumeration.

## Relationship to prior work
Xie, Sun, and Ge (2026) define \(D(q,n,R)\), prove the elementary bound \(D(q,n,R)\ge q^{n-R}/\binom nR\), and show it is asymptotically tight as \(q\to\infty\) for fixed \(n,R\). Their result specializes to \(D(q,3,1)=(1+o(1))q^2/3\), whereas the finding above is exact for every odd alphabet size. Earlier work of Lenz, Rashtchian, Siegel, and Yaakobi gives general insertion/deletion covering bounds but not this exact odd-alphabet length-three formula in the inspected material. Colbourn and Rosa provide the design-theoretic existence theorem used in the construction; their statement concerns leaves of partial triple systems rather than deletion covering codes.

## Limitations
The argument establishes the exact value only for odd \(q\). It does not settle even alphabet sizes. The proof relies on the published quadratic-leave existence theorem; the included checker verifies the coding translation and several explicit instances but is not a replacement for that theorem. Searches of the recent covering-code literature, the cited older covering-code paper, the design-theory source, and a semantic research database did not reveal the exact coding statement, but absence from those searches is not a proof that no equivalent formulation exists elsewhere.

## References
1. C. Xie, Y. Sun, and G. Ge, “New bounds for covering codes under insertions or deletions,” arXiv:2606.15379v1, 13 June 2026.
2. C. J. Colbourn and A. Rosa, “Quadratic leaves of maximal partial triple systems,” *Graphs and Combinatorics* 2 (1986), 317–337, doi:10.1007/BF01788106.
3. A. Lenz, C. Rashtchian, P. H. Siegel, and E. Yaakobi, “Covering Codes using Insertions or Deletions,” arXiv:1911.09944v4.
