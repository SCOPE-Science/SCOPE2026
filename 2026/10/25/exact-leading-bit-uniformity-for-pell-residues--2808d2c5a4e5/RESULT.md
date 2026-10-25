# Exact leading-bit uniformity for Pell residues

## Finding

Let \(P_0=0\), \(P_1=1\), and \(P_{n+1}=2P_n+P_{n-1}\) for every integer \(n\ge1\). For every pair of integers \(k,r\) with \(1\le r\le k-2\), each of the \(2^r\) dyadic intervals
\[
I_{j,k,r}=\bigl[j2^{k-r},(j+1)2^{k-r}\bigr),\qquad 0\le j<2^r,
\]
contains exactly \(2^{k-r}\) of the least residues \(P_n\bmod 2^k\), counted with their indices \(0\le n<2^k\). Equivalently, every possible string of the leading \(r\) binary digits occurs exactly \(2^{k-r}\) times in this index block.

## Assumptions and scope

All indices are integers. The recurrence is the classical Pell recurrence, and residues are represented in \(\{0,1,\ldots,2^k-1\}\). The theorem concerns the fixed block \(0\le n<2^k\); it does not assert a short-prefix distribution law, and it makes no claim of uniformity when \(r>k-2\).

## Proof

Put
\[
A=\begin{pmatrix}2&1\1&0\end{pmatrix},\qquad B=\begin{pmatrix}3&3\3&1\end{pmatrix}.
\]
For \(n\ge0\), the upper-right entry of \(A^n\) is \(P_n\). Direct multiplication gives
\[
A^4\equiv I+2^2B\pmod {2^4}.
\]
Also \(B^2\equiv0\pmod2\). Squaring the congruence and using this last divisibility proves by induction that, for every \(s\ge2\),
\[
A^{2^s}\equiv I+2^sB\pmod {2^{s+2}}.
\]
Indeed, the quadratic term \(2^{2s}B^2\) is divisible by \(2^{2s+1}\), hence by \(2^{s+3}\); the error term from the preceding congruence also vanishes modulo \(2^{s+3}\). Consequently, for odd positive \(u\),
\[
A^{u2^s}\equiv I+u2^sB\pmod {2^{s+2}}.
\]

Let \(d=u2^s\) with \(u\) odd and \(s\ge2\). Then
\[
P_{n+d}-P_n=\bigl(A^n(A^d-I)\bigr)_{12}\equiv u2^s(A^nB)_{12}\pmod {2^{s+2}}.
\]
Modulo two, \(B\) is the all-ones matrix and \(A^n\) is a permutation matrix. Thus \((A^nB)_{12}\) is odd, proving the exact valuation identity
\[
\nu_2(P_{n+d}-P_n)=s=\nu_2(d)
\]
for all \(n\ge0\) and all nonzero \(d\) divisible by four (using absolute values for negative differences).

Now fix \(k,r\) with \(1\le r\le k-2\), and put \(s=k-r\ge2\). For each \(a\in\{0,\ldots,2^s-1\}\), consider the \(2^r\) indices \(a+j2^s\), where \(0\le j<2^r\). For distinct \(j,j'\), the valuation identity gives
\[
\nu_2\bigl(P_{a+j2^s}-P_{a+j'2^s}\bigr)=s+\nu_2(j-j')<s+r=k.
\]
Therefore their residues modulo \(2^k\) are pairwise distinct. Their pairwise differences are divisible by \(2^s\), so all these residues lie in one residue class modulo \(2^s\). That class contains exactly \(2^r\) residues modulo \(2^k\), hence the selected terms occupy every one of them exactly once. Since the intervals \(I_{j,k,r}\) each contain one representative from every residue class modulo \(2^s\), each interval receives one hit for every choice of \(a\). There are \(2^s=2^{k-r}\) choices of \(a\), proving the asserted count. \(\square\)

## Verification

The proof is symbolic and establishes the quantified statement for all \(k,r\) in the stated range. The accompanying standard-library script `verify.py` checks every permitted pair \((k,r)\) for \(3\le k\le10\), and checks finite instances of the valuation identity. These computations are consistency checks, not the proof of the infinite theorem. At the excluded boundary, for example, modulo \(16\) the eight leading-three-bit bins have counts \(3,1,3,1,3,1,3,1\), so the range \(r\le k-2\) cannot be extended wholesale to \(r=k-1\).

## Relationship to prior work

Classical Pell-sequence literature studies recurrence identities and periods modulo integers. A 2016 open-access treatment of Pell polynomials and Pell sequences in groups gives periodicity and period relations, but the inspected sections do not state the exact leading-digit distribution proved here. A later discussion of Pell-prefix distribution records a one-bit half-period toggle and asks a different question about short prefixes; the present theorem extends the full-block statement to every leading-bit length \(r\le k-2\), without making a short-prefix claim. An earlier all-state cycle census for the Pell companion map counts cycles of pairs of residues, which is a different invariant and does not determine the scalar leading-bit frequencies.

## Limitations

No uniformity is claimed for \(r>k-2\), and no distribution result for prefixes shorter than \(2^k\) is proved. The theorem is specific to the classical Pell recurrence and moduli \(2^k\). The literature search was targeted rather than exhaustive; the result is not presented as a guarantee of absolute priority.

## References

1. “Power of Two as Sums of Three Pell Numbers,” arXiv:1608.06086v1, first public version 22 August 2016. The paper supplies the literature-led Pell recurrence and its 2-adic context; the leading-bit theorem above is proved here.
2. Ö. Deveci and E. Eskiyapar Saraçoğlu, “On the Pell Polynomials and the Pell Sequences in Groups,” *Chiang Mai Journal of Science* 43(1) (2016), 247–256. Open full text: https://www.thaiscience.info/Journals/Article/CMJS/10980096.pdf.
3. “The Pell Sequences in Finite Groups,” *Utilitas Mathematica* 96 (2015), 263–276. University publication record: https://avesis.atauni.edu.tr/yayin/cf206b58-0dbc-4091-995c-59b8a9f050b4/the-pell-sequences-in-finite-groups. The full text was not available through a verified lawful open-access/publisher route during this review.
4. OEIS Foundation, A000129, “Pell numbers,” https://oeis.org/A000129.
5. “Coarse well-distributedness/equidistribution of Pell sequence prefixes,” MathOverflow discussion, https://mathoverflow.net/questions/480265/coarse-well-distributedness-equidistribution-of-pell-sequence-prefixes. This later discussion is used only as a comparison for the one-bit special case and the distinct short-prefix question.
