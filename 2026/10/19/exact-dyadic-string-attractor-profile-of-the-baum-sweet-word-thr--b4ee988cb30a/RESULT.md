# Exact dyadic string-attractor profile of the Baum–Sweet word through length 512

## Finding

Let \(b=b_0b_1b_2\cdots\) denote the Baum–Sweet binary word, and let \(W_m=b_0\cdots b_{2^m-1}\). The least cardinality \(\gamma(W_m)\) of a string attractor is exactly

\[
\begin{array}{c|rrrrrrrrr}
m&1&2&3&4&5&6&7&8&9\\\hline
2^m&2&4&8&16&32&64&128&256&512\\
\gamma(W_m)&1&2&2&3&5&6&7&8&9
\end{array}
\]

All nine values have explicit finite upper and lower certificates in `baum_sweet_certificate.json`. The stated finding concerns only these nine dyadic lengths.

## Assumptions and scope

The Baum–Sweet word is defined by \(b_0=1\) and, for every integer \(t\ge1\), \(b_t=1\) if and only if **every maximal run of zeroes in the ordinary base-two representation of \(t\)** has even length. Otherwise \(b_t=0\). Positions of finite words are indexed from zero.

For a finite word \(w\) of length \(N\), a **string attractor** is a subset \(S\subseteq\{0,\ldots,N-1\}\) such that for each distinct nonempty contiguous factor \(f\) of \(w\), some occurrence \(w[i:i+|f|]=f\) has \([i,i+|f|-1]\cap S\ne\varnothing\). Write \(\gamma(w)=\min |S|\). Factors may have several occurrences and a chosen position need cross only one of them.

## Proof

For every distinct nonempty factor \(f\) of \(w\), define its *coverage set* \(U_w(f)\) as the union of all index intervals occupied by occurrences of \(f\) in \(w\). Then \(S\) is an attractor exactly when \(S\cap U_w(f)\ne\varnothing\) for every \(f\).

**Upper bound.** Each case of `baum_sweet_certificate.json` gives a sorted set `attractor_positions_zero_based`. `baum_sweet_verify.py` constructs the associated Baum–Sweet prefix independently by binary-digit inspection and by a pair-block morphism, verifies the two descriptions agree, and exhaustively compares, for each factor length, the set of all distinct factors with those having an occurrence intersecting the proposed attractor. In every case the two sets agree, proving \(\gamma(W_m)\) is at most the displayed cardinality.

**Lower bound.** Each entry `[start,length,two]` of `lower_dual_half_units_start_length_weight` denotes the distinct factor \(f=w[\texttt{start}:\texttt{start}+\texttt{length}]\) with nonnegative weight \(y_f=\texttt{two}/2\). The exact checker enumerates all occurrences of each listed factor and verifies

\[
\sum_{f:p\in U_w(f)} y_f\le1 \qquad\text{for every }p\in\{0,\ldots,N-1\}.
\]

Consequently every attractor \(S\) obeys

\[
\sum_f y_f\le\sum_f y_f\,|S\cap U_w(f)|
=\sum_{p\in S}\sum_{f:p\in U_w(f)}y_f\le |S|.
\]

The listed weights total, in increasing order of \(m\), respectively
\[
1,\;2,\;2,\;3,\;5,\;\tfrac{11}{2},\;7,\;8,\;9.
\]
Because \(|S|\) is an integer, taking ceilings gives the matching lower values \(1,2,2,3,5,6,7,8,9\). Together with the upper certificates, this proves all nine finite statements. The logical lower bound uses the exact, independently checkable dual inequality, not a claim about a solver's optimality status.

## Verification

From the directory containing both standalone artifacts, run `python3 baum_sweet_verify.py`; it uses only the Python standard library. It checks every distinct factor of every word of the nine prescribed lengths, all proposed attractor positions, and every integer-normalized dual constraint, and fails on any mismatch. For length \(512\) it checks \(108896\) distinct nonempty factors and verifies upper cardinality \(9\) and dual mass \(9\). Full totals and witnesses are machine-readable in the artifacts. The certificate-generation search process is not needed for replay.

## Relationship to prior work

The Baum–Sweet sequence originates in Baum and Sweet's 1976 work on algebraic power series. Dreyfus, Hardouin and Roques (arXiv:1507.03361, first public 2015-07-13) study generating series attached to this word, rather than its string attractors. Schaeffer and Shallit (arXiv:2012.06840, first public 2020-12-12) prove general decidability statements for automatic-sequence string attractors and explicit results for particular other sequences; the general algorithm does not itself supply the nine numerical values above. Gheeraert, Romana and Stipulanti (arXiv:2302.13647, first public 2023-02-27) study different families of morphic words. The inspected primary text did not establish this exact Baum–Sweet table; the absence of a discovered table is not a proof of global uniqueness.

## Limitations

This finding is **finite**. It does not establish \(\gamma(W_m)=m\) for \(m\ge10\), any asymptotic growth law, or a formula for arbitrary prefix lengths. The certificates have been checked in this work, but no independent external audit or literature-completeness guarantee is asserted. A prior, possibly unindexed computation remains a novelty risk.

## References

1. L. E. Baum and M. M. Sweet, *Continued Fractions of Algebraic Power Series in Characteristic 2*, Annals of Mathematics 103 (1976), 593–610.
2. T. Dreyfus, C. Hardouin and J. Roques, *Hypertranscendence of solutions of Mahler equations*, arXiv:1507.03361 (first posted 2015-07-13), https://arxiv.org/abs/1507.03361 .
3. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (first posted 2020-12-12), https://arxiv.org/abs/2012.06840 .
4. F. Gheeraert, G. Romana and M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647 (first posted 2023-02-27), https://arxiv.org/abs/2302.13647 .
