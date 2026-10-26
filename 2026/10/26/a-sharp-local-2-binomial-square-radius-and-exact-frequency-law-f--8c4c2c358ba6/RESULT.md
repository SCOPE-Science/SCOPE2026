# A sharp local \(2\)-binomial-square radius and exact frequency law for Thue–Morse

## Finding
Let \(t=t_0t_1\cdots=011010011001\cdots\) be the one-sided binary Thue–Morse word, \(t_i\equiv s_2(i)\pmod 2\). Two words are \(2\)-binomially equivalent when every binary scattered subsequence of length at most two occurs equally often in both. For each integer \(i\ge0\), define
\[
a(i)=\min\{m\ge1:t[i..i+m-1]\sim_2 t[i+m..i+2m-1]\}.\]
Then \(a(i)\) always exists and its precise range is
\[
\boxed{\{a(i):i\ge0\}=\{1,2,3,4,6,10,12,28,36\}.}
\]
In particular, the least universal bound is \(36\). The natural density of positions with \(a(i)=m\) exists and is given by:

| \(m\) | \(1\) | \(2\) | \(3\) | \(4\) | \(6\) | \(10\) | \(12\) | \(28\) | \(36\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Density | \(1/3\) | \(1/6\) | \(1/12\) | \(1/4\) | \(1/24\) | \(1/24\) | \(1/16\) | \(1/96\) | \(1/96\) |

More explicitly, put \(j=\lfloor i/128\rfloor\) and \(r=i-128j\). The worst case \(a(i)=36\) occurs **exactly** when \(r=19\), or when \(r=83\) and \(t_j=t_{j+1}\). Hence it occurs with density \(1/96\).

## Assumptions and scope
Indices start at zero, the two blocks are adjacent contiguous factors, and subsequence multiplicities use increasing (not necessarily adjacent) positions. The root \(m\) is a positive integer. The infinite word is the fixed point of \(\mu(0)=01,\mu(1)=10\), with \(t_0=0\). Densities are natural densities along starting indices \(i=0,1,\ldots\); there is no quotient by rotation or reversal. The proof is a complete finite-reduction proof for this infinite word; it does not claim the same bound for arbitrary automatic words.

## Proof
**1. A two-number signature.** For any binary block \(w=w_0\cdots w_{m-1}\), put \(k(w)=\sum_h w_h\) and \(S(w)=\sum_{h=0}^{m-1}h w_h\). The scattered-subsequence count of `01` is \(S(w)-\binom{k(w)}2\), because the \(r\)-th one has its zero predecessors counted by its position minus the preceding \(r\) ones. The counts of `0`, `1`, `00`, and `11` are determined by \(m\) and \(k(w)\); the count of `10` is \(k(w)(m-k(w))\) minus that of `01`. Thus, for equal-length blocks, \(2\)-binomial equivalence is **equivalent** to equality of their two integer signatures \((k,S)\). This identity handles all root lengths, including \(m=1\).

**2. Exhaustive reduction for an infinite word.** Put \(B=128=2^7\). For each \(xy\in\{00,01,10,11\}\), form the explicit \(256\)-letter word \(\mu^7(xy)\). For each offset \(0\le r<128\), take its length-\(72\) factor beginning at \(r\), and compute the first \(m\in\{1,\ldots,36\}\) for which the two successive length-\(m\) blocks have equal \((k,S)\). These are exactly \(4\cdot128=512\) cases. Every binary pair occurs in the source Thue–Morse word. Every starting index is uniquely \(i=128j+r\), with \(0\le r<128\), so the length-\(72\) factor at \(i\) is exactly the corresponding factor of \(\mu^7(t_jt_{j+1})\). Therefore the finite computation covers **every starting position**, not merely a tested prefix.

The complete counts of least roots for each source pair, in the order of columns shown, are:

| Source pair | \(1\) | \(2\) | \(3\) | \(4\) | \(6\) | \(10\) | \(12\) | \(28\) | \(36\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `00` | 42 | 22 | 12 | 32 | 4 | 6 | 8 | 0 | 2 |
| `01` | 43 | 21 | 10 | 32 | 6 | 5 | 8 | 2 | 1 |
| `10` | 43 | 21 | 10 | 32 | 6 | 5 | 8 | 2 | 1 |
| `11` | 42 | 22 | 12 | 32 | 4 | 6 | 8 | 0 | 2 |

Each row totals \(128\). No root is missing. The six cases of root \(36\) are precisely source pair/offset \((00,19),(00,83),(01,19),(10,19),(11,19),(11,83)\); therefore the sharpness and position characterization hold. In particular, at index \(i=19\), the consecutive length-\(36\) blocks are `101100110100110010110011010010110100` and `110010110100101100110100101101001100`. Both have signature \((18,297)\), and no smaller positive root works.

**3. Exact densities.** The limiting frequencies of adjacent source pairs are
\[
(f_{00},f_{01},f_{10},f_{11})=(1/6,1/3,1/3,1/6).
\]
For completeness, substituting a word gives internal pairs `01` once per original zero and `10` once per original one; the boundary pair contributed by a source pair \(xy\) is \((1-x)y\). On normalized frequencies the substitution recurrence becomes
\[
(f'_{00},f'_{01},f'_{10},f'_{11})=
\tfrac12(f_{10},f_{11},f_{00},f_{01})+(0,\tfrac14,\tfrac14,0).
\]
The map is contracting and has precisely the fixed point displayed. Thue–Morse's dyadic block decomposition extends the limiting frequencies from substitution-level prefixes to arbitrary prefixes (equivalently, standard unique ergodicity of this primitive substitution). For a given offset \(r\), the occurrence density of a source pair \(xy\) is \(f_{xy}/128\). Weighting the displayed \(512\)-case table by these four frequencies gives the stated nine rational densities, summing to one. In particular, the worst-case density is \(1/128+(f_{00}+f_{11})/128=1/96\).

**4. Completeness and independent checks.** The file `templates.csv` lists every source pair, offset, and exact least root. The standalone `verify.py` regenerates the \(512\) entries directly from the substitution, independently counts all six scattered-subsequence types for each candidate root, checks agreement with the \((k,S)\) criterion, checks the full table and densities, and verifies the sharp witness. Its independent binary-digit-sum implementation of the infinite word also tests the complete length-\(72\) factor set and \(8192\) individual starting positions. The finite certificate exhaustively checks the complete set of possible local factors, so the argument proves an infinite-word claim without extrapolation.

## Verification
Run `python3 verify.py` in the folder containing `verify.py` and `templates.csv` with Python \(\ge3.10\). The program depends only on the standard library, reads the embedded CSV, and exits unsuccessfully on any mismatch. It verifies all \(512\) possible aligned cases, independently computes scattered subsequences, and checks the exact spectrum. The arbitrary-prefix tests corroborate the algebraic completeness proof; the latter is established by the length-\(128\) block decomposition, not by a bounded-prefix experiment.

## Relationship to prior work
Rigo and Salimov (2013) introduced binomial complexity and studied the Thue–Morse word at the level of factor equivalence classes; they also posed avoidance questions for \(2\)-binomial squares. Rao, Rigo, and Salimov (2015) investigated square/cube avoidability and constructed other infinite words that avoid the patterns. Lejeune, Leroy, and Rigo (2020) evaluated the *number of binomial equivalence classes of fixed-length factors* of Thue–Morse. Those quantities do not determine which **adjacent** block pairs match at a specified starting index or the least matching root there. In particular, a global root-length existence spectrum does not imply a sharp all-start minimum or its position densities. The present finding addresses that distinct local question.

## Limitations
The proof is computer-assisted at one explicit finite \(512\)-template table and requires checking the accompanying independent executable certificate. It gives the complete least-root distribution, but not the number of larger-root \(2\)-binomial squares beginning at each position, nor analogues for other infinite words. Priority is assessed against the inspected sources only, not certified against every unpublished calculation.

## References
1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (2013), publicly available since 2013-05-27, https://orbi.uliege.be/handle/2268/149313 ; full preprint https://orbi.uliege.be/bitstream/2268/149313/2/binomial_final_long.pdf .
2. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes* (2015), https://orbi.uliege.be/bitstream/2268/178702/1/final.pdf .
3. M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word* (preprint available 2019; journal 2020), https://orbi.uliege.be/bitstream/2268/234006/1/binomial-TM-lastVersion.pdf .
