# Complete minimal-absent-factor basis of the binary powers-of-two indicator

## Finding

For the infinite binary word \(w=w_0w_1\cdots\) defined by \(w_i=1\) precisely when \(i=2^j\) for an integer \(j\ge0\), the set \(\mathcal M(w)\) of all **minimal absent contiguous factors** is exactly

\[
\begin{aligned}
\mathcal M(w)={}&\{111,0011,1011\}\\
&\cup\{1 0^{d-1}1:d\ge1,\ d\text{ is not a power of two}\}\\
&\cup\{0^{2^{k-1}}1 0^{2^k-1}1:k\ge1\}\\
&\cup\{1 0^{2^k-1}1 0^{2^{k+1}}:k\ge0\}.
\end{aligned}
\]

Consequently, for every integer \(n\ge2\), the number \(m(n)\) of distinct minimal absent factors of length \(n\) is

\[
m(n)=\mathbf1_{n=3}+2\mathbf1_{n=4}+\mathbf1_{n-1\notin\{2^j:j\ge0\}}+2\mathbf1_{n\in\{3\cdot2^j+1:j\ge0\}}.
\]

In particular \(m(1)=0\); the first counts \(m(2),\ldots,m(16)\) are \(0,1,5,0,1,3,1,0,1,1,1,3,1,1,1\). The two non-geometric boundary families produce spikes at lengths \(4,7,13,25,49,\ldots\).

## Assumptions and scope

Indices start at zero, so the support of \(w\) is \(\{1,2,4,8,\ldots\}\). For a binary word \(u\), \(0^a\) denotes \(a\) consecutive zeros, with \(0^0\) empty. A factor occurs at a finite nonnegative starting index. An absent word \(u\) of length \(\ell\ge2\) is **minimal absent** when both its length-\((\ell-1)\) prefix and length-\((\ell-1)\) suffix occur; this is equivalent to every proper contiguous factor occurring. The empty word and every one-letter word occur; hence there are no length-one minimal absent factors. The theorem concerns distinct strings, not their multiplicities or scattered subsequences.

## Proof

**Step 1: elementary occurrence constraints.** The ones occur at increasing positions \(2^j\), so each consecutive pair of ones has distance exactly \(2^j\), uniquely for that \(j\). Any contiguous factor containing two or more ones therefore occurs **at most once**, because it contains at least one entire consecutive-one pair; its distance determines that pair's unique position, and the factor's relative offset determines its starting position. Conversely, every word with at most one one occurs: the all-zero runs are unbounded, while for any fixed numbers \(a,b\ge0\), a sufficiently large power-of-two position has at least \(a\) consecutive zeros immediately before it and at least \(b\) after it.

**Step 2: at most three ones.** Write a minimal absent word of length at least two as \(u=a v b\) with letters \(a,b\). If \(v\) had two or more ones, the occurring prefix \(av\) and occurring suffix \(vb\) would both align their shared \(v\) at its unique occurrence. Their outer letters would then give an occurrence of \(avb\), a contradiction. Thus \(v\) has at most one one. A minimal absent word cannot have fewer than two ones (Step 1), and if it has three, both endpoint letters are ones.

**Step 3: the three-one case.** It must have the shape \(u=1 0^{2^i-1}1 0^{2^j-1}1\) for some integers \(i,j\ge0\), because its prefix and suffix each contain an adjacent pair of ones. If \(j\ge1\), the prefix ending just before the final one occurs only if the zero-run after the second one has length at most \(2^{i+1}-1\), yielding \(j\le i+1\). The suffix beginning just after the first one occurs only if the zero-run before the first one of its terminal pair has length at most \(2^{j-1}-1\), yielding \(i\le j-1\). Hence \(j=i+1\), in which case the triple occurs at positions \(2^i,2^{i+1},2^{i+2}\). If \(j=0\), the terminal pair is uniquely at positions \(1,2\), preceded by precisely one zero; the suffix can occur only when \(2^i-1\le1\), namely \(i\in\{0,1\}\). These produce exactly \(111\) and \(1011\), both absent and with occurring proper prefix and suffix.

**Step 4: the two-one case, both endpoints ones.** A candidate \(u=1 0^{d-1}1\) occurs exactly when \(d\) is a power of two. For every positive \(d\), its one-letter-deleted prefix and suffix occur because zeros after and before a sufficiently isolated one can be arbitrarily long. Thus this case gives exactly the stated non-power-of-two family.

**Step 5: the two-one case, initial zero.** The only remaining possibility ending in one is \(u=0^a1 0^{2^k-1}1\) with \(a\ge1\) and \(k\ge0\), because the suffix must contain an adjacent pair of ones. For \(k\ge1\), this pair starts at \(2^k\), preceded by exactly \(2^{k-1}-1\) consecutive zeros. Thus \(u\) is absent but its suffix after deleting its first zero occurs if and only if \(a=2^{k-1}\). The prefix after deleting its final one always occurs at a sufficiently large isolated one, giving the stated left-overhang family. For \(k=0\), the unique pair is at positions \(1,2\), with exactly one preceding zero at position zero; the same argument gives \(a=2\), i.e. the exceptional \(0011\).

**Step 6: the two-one case, terminal zero.** The word has shape \(u=1 0^{2^k-1}1 0^b\), with integers \(k\ge0,b\ge1\). The adjacent-one pair has exactly \(2^{k+1}-1\) zeros after its second one. It therefore becomes absent for the first time at \(b=2^{k+1}\), while its prefix with the final zero removed still occurs. Its suffix with the first one removed occurs at a sufficiently isolated one. This gives precisely the right-overhang family.

If both endpoint letters were zero, the two ones would both lie within \(v\), contrary to Step 2. The cases exhaust all possible minimal absent factors. All stated families satisfy absence and the required two one-letter-deletion occurrence conditions. This proves the classification.

For the length formula, the isolated exceptions contribute one at length three and two at length four; the endpoint-one family has exactly one member at each length \(n\ge2\) for which \(n-1\) is not a power of two; the left and right families each contribute exactly one at every length \(3\cdot2^j+1\), for \(j\ge0\). Different strings in the families have different endpoint patterns, so counts add without duplication.

## Verification

A standalone standard-library Python checker, `checker.py`, generates an independent large prefix and enumerates its factor sets for every length from one through 160. For each length, it enumerates all absent one-letter extensions of occurring length-minus-one factors and retains precisely those whose opposite length-minus-one factor also occurs. It compares these sets against the four explicit families. Run from the directory containing the two files with `python3 checker.py`. The run passed with 166 matched minimal-absent instances for lengths 2 through 160. This finite comparison is a check, **not** the proof for all lengths, which is given above.

## Relationship to prior work

Gheorghiciuc's study of infinite gap-increasing binary words (arXiv:math/0512256, first posted 2005-12-13) gives their subword-complexity framework and factor-count identities. Pinho, Ferreira, Garcia and Rodrigues (2009) formalize minimal absent words and algorithms for their enumeration in finite sequences. Mignosi, Restivo and Sciortino (2002) examine forbidden factors of infinite words, including Sturmian families. The present theorem specializes to the powers-of-two indicator and **classifies the complete infinite minimal-absent set and its exact length profile**, which is not implied by the inspected factor-complexity formulas or general minimal-absence algorithms. A complete historical-priority assessment is not claimed.

## Limitations

This statement is for the one-sided infinite characteristic word with ones at positive powers of two, including the initial zero at position zero. Changing the initial boundary changes exceptional minimal absent words. The classification does not automatically extend to other sparse supports, finite prefixes, or minimal absent *subsequences*. The published 2002 forbidden-factor article was located by citation and abstract, but its author-hosted full text could not be retrieved; this leaves historical-priority uncertainty. All conclusions are supported by a mathematical proof plus finite computational checks, without independent validation.

## References

1. I. Gheorghiciuc, *The subword complexity of a class of infinite binary words*, arXiv:math/0512256v1 (13 December 2005), https://arxiv.org/abs/math/0512256.
2. A. J. Pinho, P. J. S. G. Ferreira, S. P. Garcia and J. M. O. S. Rodrigues, *On finding minimal absent words*, BMC Bioinformatics 10, 137 (8 May 2009), https://doi.org/10.1186/1471-2105-10-137.
3. F. Mignosi, A. Restivo and M. Sciortino, *Words and forbidden factors*, Theoretical Computer Science 273 (2002), https://doi.org/10.1016/S0304-3975(00)00436-9.
