# Independent mathematical audit

## correctness

PASS

For n>=3, 2<=k<n and m>=2|k, the gaps of S=<n,n+1,...,n+k> are precisely intervals [t(n+k)+1,(t+1)n-1] for t=0,...,L-1 with L=ceil((n-1)/k). Comparing to blocks [tn+1,(t+1)n-1] deletes tk/m of each residue, yielding N_r=count(1<=x<Ln;x=r mod m)-count(1<=t<L;tn=r mod m)-(k/m)*C(L,2). For gcd(n,m)=1, both uncorrected counts have spread <=1, hence sharp spread <=2; explicit n=2m-1,k=m achieves 2 for m>=4. Polynomial cyclic derivative shows equidistribution iff gcd(n,m)=1 and (n=1 mod m or L=0 mod m), using nontrivial proper cyclic arcs without translation symmetry. Special m=2,3 and m|n cases follow by explicit incomplete-block/resonance counts. All statements require m|k.

## originality

PASS

Shor 2021 gives an Apéry-multiset equidistribution criterion and various special generator configurations, which must be credited. The new derivation gives a concrete all-interval-width residue histogram, sharp general spread bounds and resonance classification; an indirect consequence of a published generic Apéry formula may cover portions of the claim but no stronger exact family statement was found in inspected theorem sections.

## value

PASS

Determines a natural complete residue-gap invariant and exactly when gaps balance for an infinite, widely studied generator family; the sharp universal discrepancy and unbounded resonance quantify arithmetic behavior beyond standard genus/Frobenius numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
