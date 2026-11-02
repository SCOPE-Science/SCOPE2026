# Sharp read-length reconstruction of binary three-marker necklaces

## Finding

Let \(n\ge3\), and let \(\mathcal N_{n,3}\) be the set of binary cyclic words of length \(n\) containing exactly three occurrences of the symbol \(1\), identified only under cyclic rotation, **not** under reversal. For \(1\le k\le n\), the cyclic \(k\)-multispectrum \(\mathcal S_k(W)\) is the multiset of the \(n\) length-\(k\) factors starting at each cyclic position, including multiplicities. Let \(R(n)\) be the least \(k\) for which the map \(W\mapsto\mathcal S_k(W)\) is injective on \(\mathcal N_{n,3}\).

**Theorem (sharp uniform threshold and individual chirality threshold).** The exact uniform reconstruction threshold is
\[
R(n)=\begin{cases}
1,&n=3,4,\\
2,&n=5,\\
\lfloor 2n/3\rfloor,&n\ge6.
\end{cases}
\]
Furthermore, write a representative of \(W\) as \(1 0^a1 0^b1 0^c\), where \(a,b,c\) are nonnegative and \(a+b+c=n-3\). If these three gaps are pairwise distinct and \(M=\max(a,b,c)\), then the *individual* shortest read length uniquely identifying \(W\) among **all** members of \(\mathcal N_{n,3}\) is exactly
\[
\rho(W)=n-M.
\]
For every shorter length \(k<n-M\), the distinct reverse necklace has **exactly the same** cyclic \(k\)-multispectrum. At length \(n-M\), a read containing all three markers certifies their cyclic ordering and hence identifies the entire necklace.

## Assumptions and scope

The alphabet is \(\{0,1\}\). The length \(n\) and the promise of exactly three ones are known. All \(n\) cyclic starting positions are observed, with multiplicity; factor orientation is retained. A necklace and its reverse are distinct unless one is a rotation of the other. The theorem includes adjacent ones (zero-length gaps) and periodic necklaces. There is no probabilistic hypothesis and no requirement that all windows be distinct.

Set \(x\le y\le z\) to be the three gaps in nondecreasing order. Then \(x+y+z=n-3\), and the shortest cyclic factor containing all three distinct marked positions has length
\[
x+y+3=n-z.
\]
Indeed, such a factor traverses two consecutive gaps and chooses the two smallest of the three, which are consecutive around a triangle.

## Proof

**1. Monotonicity and factor marginalization.** Given \(\mathcal S_k(W)\), counting all length-\(k\) factors with a prescribed length-\(\ell\) prefix recovers the full cyclic \(\ell\)-factor multiplicities, for every \(1\le\ell\le k\). Thus identifiability is monotone in \(k\). For every \(d\ge0\), the count of the factor \(10^d1\) is precisely the number of zero gaps of length \(d\), provided \(d+2\le k\). The intervening zeros force the two ones to be consecutive cyclic markers.

**2. Reversal invisibility below the shortest triple-marker factor.** We prove that any three-marker necklace and its reversal have identical \(k\)-multispectra when \(k\le x+y+2\). If two gaps coincide, the gap triple is rotationally equivalent to its reversal, so the necklaces themselves already agree. Thus assume \(x<y<z\). Every observed factor then contains at most two ones.

Factors containing no ones have the form \(0^k\), whose multiplicity is \(\sum_{d\in\{x,y,z\}}\max(0,d-k+1)\); this depends only on the unordered gap multiset.

A factor containing one one has the form \(0^u10^v\), with \(u+v+1=k\). If the gaps around the central one are \(d\) (before) and \(e\) (after), its multiplicity contributes \(\mathbf1_{u\le d}\mathbf1_{v\le e}\). On reversing the word, the three directed adjacencies of the ordered gap triple reverse. The sum of these three indicators can change only if the threshold sets \(\{d:d\ge u\}\) and \(\{d:d\ge v\}\) distinguish two different nontrivial upper levels of the ordered triple \(x<y<z\). That requires one threshold at least \(x+1\) and the other at least \(y+1\). Consequently \(u+v\ge x+y+2\), contradicting \(k=u+v+1\le x+y+2\). A fully explicit way to see this is that threshold sets of sizes \(0\) or \(3\) are orientation-independent, equal sets of size \(1\) or \(2\) are also orientation-independent, and the only potentially asymmetric case has strict nested sizes \(1\) and \(2\).

A factor containing two ones is necessarily \(0^u10^d10^v\), with \(d\) one of the three gaps. Let \(e,f\) be the other two gaps. In the two opposite orientations, its possible contributions are respectively \(\mathbf1_{u\le e}\mathbf1_{v\le f}\) and \(\mathbf1_{u\le f}\mathbf1_{v\le e}\), up to consistently exchanging \(e,f\). An inequality between them requires \(\max(u,v)\ge\min(e,f)+1\). Therefore its length is at least \(d+\min(e,f)+3\ge x+y+3\), again impossible. This comparison applies separately to each distinct interior gap \(d\).

No factor with three ones exists below length \(x+y+3\). These cases exhaust all binary factors, proving the reversal invisibility lemma.

**3. Sharp individual threshold for pairwise distinct gaps.** Such a necklace is not rotationally equivalent to its reverse. By step 2 its reverse gives a genuine ambiguity at all \(k<n-z\). At \(k=n-z=x+y+3\), the spectrum contains a word with three ones, with internal gaps \(x,y\) in their actual cyclic order, namely one of \(10^x10^y1\) or \(10^y10^x1\). The two internal gaps read off from this factor, together with the remaining gap \(n-3-x-y\), determine the cyclic gap triple up to rotation. Any other three-marker necklace having the same spectrum must therefore be the same necklace. Thus \(\rho(W)=n-z\).

**4. Uniform upper bound for \(n\ge6\).** Put \(K=\lfloor2n/3\rfloor\). If a necklace has a length-\(K\) factor containing all three ones, that factor already determines the necklace as in step 3. If it has no such factor, its largest gap satisfies \(z\le n-K-1\). Writing \(n=3m+r\), with \(r\in\{0,1,2\}\), yields exactly the following possibilities for the unordered gap multiset:

- For \(r=0\): \(n=3m\), \(K=2m\), and the sole possibility is \(\{m-1,m-1,m-1\}\).
- For \(r=1\): \(n=3m+1\), \(K=2m\), and the possibilities are \(\{m,m,m-2\}\) or \(\{m,m-1,m-1\}\).
- For \(r=2\): \(n=3m+2\), \(K=2m+1\), and the sole possibility is \(\{m,m,m-1\}\).

All the cases above have at least two equal gaps, so an unordered gap multiset determines exactly one rotation class. Since \(n\ge6\), in every listed case \(K\ge z+2\), and the counts of \(10^d1\) recovered from the length-\(K\) spectrum identify every gap multiplicity. Hence all necklaces are identified by \(K\)-reads, including the nonprimitive equally spaced case.

**5. Sharp lower bound for \(n\ge6\).** In each residue class take a triple with distinct nonnegative gaps \(x<y<z\) as follows:
\[
\begin{array}{c|ccc|c}
n&x&y&z&n-z\\ \hline
3m&m-2&m-1&m&2m\\
3m+1&m-2&m-1&m+1&2m\\
3m+2&m-2&m&m+1&2m+1
\end{array}
\qquad(m\ge2).
\]
The total length in each row is \(x+y+z+3=n\), and \(n-z=\lfloor2n/3\rfloor=K\). Step 2 gives two distinct reversal necklaces with identical length-\((K-1)\) spectra. Thus \(R(n)>K-1\), and step 4 gives equality.

**6. Small lengths.** For \(n=3,4\) there is just one weight-three necklace, so \(R(n)=1\). For \(n=5\) there are two necklaces, with gap multisets \(\{0,0,2\}\) and \(\{0,1,1\}\). Their one-letter decks agree because both have three ones and two zeros, while their two-letter decks differ in the number of factors \(11\) (respectively \(2\) and \(1\)). Therefore \(R(5)=2\). The proof is complete.

## Verification

Run `python3 verify.py` in a standard Python installation. The standalone verifier uses only the standard library. It enumerates **all** weight-three binary rotation classes for \(3\le n\le25\) and every \(k\) up through the asserted global threshold; it checks every chiral necklace for \(6\le n\le50\) at both sides of its proposed individual threshold. It separately validates \(189\) explicitly parameterized sharpness pairs up to length \(194\), and reconstructs all \(1356\) weight-three necklaces for \(6\le n\le30\) by the two branches of the proof's constructive decoder.

Observed output:

```text
VERIFY_OK exhaustive_necklaces=772 exact_all_length_thresholds_n=3..25 chiral_orientation_cases=5944 explicit_sharpness_pairs=189 decoder_cases=1356 spectrum_comparisons=22010
```

The finite checks do not prove the all-length result; steps 1–6 supply its general proof. No randomized experiment, theorem prover, remote service, or third-party certificate is needed.

## Relationship to prior work

Ota and Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, first publicly available in advance publication on September 5, 2023, give a general weighted-automaton reconstruction criterion and an algorithm to seek a minimal read length. Their setting includes arbitrary binary circular strings under a primitivity assumption, but the inspected article does not state the present closed-form worst-case read length on the three-marker stratum, nor the exact pointwise chirality obstruction; the equal-gap periodic case here also lies outside their primitivity assumption. The new theorem is therefore a sharp analytical specialization with a separate sparse-gap proof, not a claim to have invented cyclic-substring reconstruction.

Marcovich and Yaakobi, *Reconstruction of Strings from their Substrings Spectrum* (first arXiv version December 23, 2019), study linear read multispectra and reconstruction-code constructions in lossy/noisy models, rather than this exact rotation-class identifiability problem. The standard substring-uniqueness sufficient condition (attributed there to Ukkonen) does not give the asserted necessary and sufficient three-marker thresholds. General Eulerian assembly and graph-walk methods likewise do not by themselves supply the explicit two-thirds law or the reversal invisibility mechanism.

## Limitations

Only **three** ones, full multiplicity information, oriented reads, known length, and exact noiseless observations are treated. There is no claimed threshold for four or more ones, unknown weight, unordered composition reads, missing reads, or sequencing errors. The individual formula is asserted only for pairwise distinct gap lengths; a necklace with repeated gaps can have a shorter individual reconstruction threshold, as the verifier examples demonstrate. Research discovery cannot exclude an obscure equivalent published specialization or an implicit closed-form consequence not recognized during source inspection. The work has not undergone independent scientific validation.

## References

1. Takahiro Ota and Akiko Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences, E107.A(3), 409–416 (2024); advanced online September 5, 2023. DOI: 10.1587/transfun.2023TAP0015. Open primary text: https://www.jstage.jst.go.jp/article/transfun/E107.A/3/E107.A_2023TAP0015/_pdf/-char/en
2. Sagi Marcovich and Eitan Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108, first submitted December 23, 2019. Full text: https://arxiv.org/html/1912.11108v2
3. Carl Kingsford, Michael C. Schatz and Mihai Pop, *Assembly complexity of prokaryotic genomes using short reads*, *BMC Bioinformatics* **11**, 21 (January 12, 2010). DOI: 10.1186/1471-2105-11-21. Open full text: https://link.springer.com/article/10.1186/1471-2105-11-21. The directed multigraph/Euler-tour framework in this paper is prior art, and the sparse binary three-marker theorem here does not claim that framework.
